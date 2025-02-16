
from xml.etree.ElementTree import ElementTree , ParseError , parse , indent
from urllib.parse import urljoin
from os.path import exists , dirname , abspath
from copy import copy
from sys import exit , stderr
from os import makedirs


Include_Tag = '{http://www.w3.org/2001/XMLSchema}include'

Output = '.build/Schema.xsd'
Input = 'Source/mod.xsd'

Max_Depth = 6


files = set()


def resolveIncludes ( parent , base , depth ):

    if depth == 0 :
        raise SyntaxError( f'Maximum inclusion depth reached!' , Max_Depth )


    index = 0

    while index < len(parent) :

        element = parent[ index ]


        if element.tag != Include_Tag :

            resolveIncludes(element,base,depth)

            index += 1

            continue


        file = element.get('schemaLocation')

        print( f'Including file : { file }' )

        file = urljoin(base + '/', file)

        if file in files :

            parent.remove(element)

            continue

        files.add(file)

        with open(file,'rb') as handle :
            node = parse(handle).getroot()

        if node is None :
            raise SyntaxError( f' Failed to find root in included file!\n%s' % file )

        node = copy(node)

        resolveIncludes(node,dirname(file),depth - 1)

        node.tail = ( node.tail or '' ) + ( element.tail or '' )


        if 'schema' in node.tag :

            parent.remove(element)

            for item in node :
                parent.insert(index,item)

            index += len(node)

        else :

            parent[ index ] = node

            index += 1


def makeBuildFolder ():

    folder = dirname(Output)

    if exists(folder) :
        return

    print('Creating .build folder')

    makedirs(folder)


def writeSchema ( tree : ElementTree , path : str ):

    print( f'Writing schema to : { path }' )

    indent (
        space = '    ' ,
        level = 0 ,
        tree = tree
    )

    tree.write (
        file_or_filename = path ,
        xml_declaration = True ,
        encoding = 'utf-8'
    )


def main ():

    try :

        input_path = abspath(Input)
        base_dir = dirname(input_path)

        makeBuildFolder()

        tree = parse(input_path)

        root = tree.getroot()

        resolveIncludes(root,base_dir,Max_Depth)

        writeSchema(tree,Output)

        exit(0)
        return

    except ParseError as exception :

        print( f'Failed to parse XML : { exception }' , file = stderr )

    except Exception as exception :

        print( f'Error : { exception }' , file = stderr )

    exit(1)


if __name__ == '__main__' :
    main()



