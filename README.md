
# Addon Manifest Schema

This repository contains the source files for the XML  
Schema ( XSD ) used for the [FreeCAD Addon Manifest].

<br/>

## Repository

| Folder | Purpose |
|:-------|:--------|
| `Source`  | Tree or bite sized XSD source files.
| `Scripts` | Python scripts used to bundle the XSD files.
| `.build`  | Created when you run the bundle script.

<br/>

## Bundling

The schema can be used as is by referencing `Source/mod.xsd`

If you need a single file instead you can bundle the  
files in `Source` with the following python command:

```sh
python Scripts/Bundle.py
```

This will create a bundled file at `.build/Schema.xsd`

<br/>

## Usage

The following demonstrates how to reference the schema.

```xml
<?xml 
    version = '1.0'
    encoding = 'UTF-8'
    standalone = 'no'
?>
<?xml-model
    schematypens = 'http://www.w3.org/2001/XMLSchema'
    href = '<Schema Url>'
?>
<package format = '1' >
    <!-- . . . -->
</package>
```

<br/>

## Workarounds

Due to the missing [**XSD 1.1 Support**][Support] in the RedHat  
VSCode extension, multiple workarounds are being  
used to approximate the actual schema structure.

-   In XSD 1.1, the `<all>` tag allows for `unbound` elements, the two possible  
    workarounds are using a `sequence` and forcing the order of elements or  
    using `<choice>` and allowing multiple of every tags.

    The `<package>` tag uses the latter to facilitate `<maintainer>` & `<url>`
    


[FreeCAD Addon Manifest]: https://wiki.freecad.org/Package_Metadata
[Support]: https://github.com/redhat-developer/vscode-xml/issues/222