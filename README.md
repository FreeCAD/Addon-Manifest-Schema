





## Workarounds

Due to the missing [**XSD 1.1** support][Support] in the RedHat  
VSCode extension, multiple workarounds are being  
used to approximate the actual schema structure.

-   In XSD 1.1, the `<all>` tag allows for `unbound` elements, the two possible  
    workarounds are using a `sequence` and forcing the order of elements or  
    using `<choice>` and allowing multiple of every tags.

    The `<package>` tag uses the latter to facilitate `<maintainer>` & `<url>`
    


[Support]: https://github.com/redhat-developer/vscode-xml/issues/222