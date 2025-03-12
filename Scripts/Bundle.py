
from xml.etree.ElementTree import ElementTree , ParseError , parse , indent
from urllib.parse import urljoin
from os.path import dirname , relpath , exists , join , sep
from copy import copy
from sys import exit , stderr
from os import makedirs


Include_Tag = '{http://www.w3.org/2001/XMLSchema}include'

Project_Path = dirname(dirname(__file__))
Output_Path = join(Project_Path,'.build','Schema.xsd')
Source_Path = join(Project_Path,'Source')
Input_Path = join(Source_Path,'mod.xsd')

Max_Depth = 7


files = set()


def resolveIncludes ( parent , base , depth = Max_Depth ):

    if depth == 0 :
        raise SyntaxError( f'Maximum inclusion depth reached! ( Max Depth : { Max_Depth } )' )

    index = 0

    while index < len(parent) :

        element = parent[ index ]

        if element.tag != Include_Tag :
            resolveIncludes(element,base,depth)
            index += 1
            continue

        file = element.get('schemaLocation')

        file = urljoin( base + sep , file )

        relative = relpath(file,Source_Path)

        if relative in files :
            parent.remove(element)
            continue

        print( f'+ 📄 { relative }' )

        files.add(relative)

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


def resolveIncludeTree ( tree ):

    print( f'Resolving includes:' )

    base = dirname(Input_Path)

    root = tree.getroot()

    resolveIncludes(root,base)

    print()
    print( f'Resolved { len(files) } includes.')
    print()


def makeBuildFolder ():

    folder = dirname(Output_Path)

    if exists(folder) :
        return

    print('Creating `.build` folder')
    print()

    makedirs(folder)


def writeSchema ( tree : ElementTree , path : str ):

    print( f'Writing bundled schema.' )
    print()

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

    print( f'Bundling multiple XSD files into one.' )

    print( f'Project Folder : { Project_Path }' )
    print( f'Entrypoint : { relpath(Input_Path,Project_Path) }' )
    print( f'Bundle : { relpath(Output_Path,Project_Path) }' )

    print()

    try :

        makeBuildFolder()

        tree = parse(Input_Path)

        resolveIncludeTree(tree)

        tree.getroot().set('xmlns','HTTPS://Addons.FreeCAD.Org/Manifest')

        writeSchema(tree,Output_Path)

        print( f'Done.' )

        exit(0)
        return

    except ParseError as exception :

        print( f'Failed to parse XML : { exception }' , file = stderr )

    except Exception as exception :

        print( f'Error : { exception }' , file = stderr )

    exit(1)


if __name__ == '__main__' :
    main()
