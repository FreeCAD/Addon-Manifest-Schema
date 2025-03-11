
[![Button Overview]][Overview]

<br/>

# 🔧 Development

The source files of the schema can be used  
directly by referencing `Source/mod.xsd`.

```xml
<?xml-model
    href = '/Path-To-Cloned-Repository/Source/mod.xsd'
?>
<package
    xmlns = 'HTTPS://Addons.FreeCAD.Org/Manifest'
>
```

<br/>

<!----------------------------------------------------------------------------->

## 📦 Bundling

To bundle the `/Source/` files into a combined schema,  
you just have to run the following Python command:

```sh
python Scripts/Bundle.py
```

This will create a bundled file at `.build/Schema.xsd`

<!----------------------------------------------------------------------------->

### 📜 Preview

[![Bundler Showcase 1]](#)

<br/>

<!----------------------------------------------------------------------------->

[Bundler Showcase 1]: ../Assets/Images/Bundler-Showcase-1.webp

[Button Overview]: https://img.shields.io/badge/🢐_Back-418FDE?style=for-the-badge

[Overview]: ./README.md
