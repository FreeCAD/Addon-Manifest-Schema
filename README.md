
<div align = center >

# Addon Manifest Schema

This repository contains the source files for the XML  
Schema ( XSD ) used for the [FreeCAD Addon Manifest].

[![Button Discord]][Discord]  
[![Button Website]][Website]  
[![Button Contribute]][Contribute]

</div>

<br/>

<!----------------------------------------------------------------------------->

## 📷 Showcase

The schema not only provides validation, autocomplete  
and examples but also tooltips, here is one of them.

<img width = 500 src = './Assets/Images/Dependency-Greater-Than-Equal.webp' />

<br/>

<!----------------------------------------------------------------------------->

## 💬 Usage

Use the following snippet to reference  
this schema in your `<package>` tag.

```xml
<package
    Manifest:schemaLocation = 'HTTPS://Addons.FreeCAD.Org/Manifest https://Addons.FreeCAD.Org/Manifest'
    xmlns:Manifest = 'http://www.w3.org/2001/XMLSchema-instance'
    xmlns = 'HTTPS://Addons.FreeCAD.Org/Manifest'
>
```

<br/>

<!----------------------------------------------------------------------------->

### 📍 Endpoints

Currently FreeCAD only supports one endpoint  
that hosts the **latest** version of the schema at:

```md
https://Addons.FreeCAD.Org/Manifest.xsd
```

<br/>

<!----------------------------------------------------------------------------->

### 💾 Older Versions

In case you need to use an older version of the schema,  
you can reference one of the [GitHub Releases] like so:

```md
https://github.com/FreeCAD/FreeCAD-Addon-Manifest-Schema/releases/download/<Version>/Schema.xsd
```

```md
https://github.com/FreeCAD/FreeCAD-Addon-Manifest-Schema/releases/download/v1.0/Schema.xsd
```

<br/>

<!----------------------------------------------------------------------------->

### 📄 Integration

The following code demonstrates how you can  
reference this schema in your addon manifest:

```xml
<?xml
    version = '1.0'
    encoding = 'UTF-8'
    standalone = 'no'
?>
<package
    Manifest:schemaLocation = 'HTTPS://Addons.FreeCAD.Org/Manifest https://Addons.FreeCAD.Org/Manifest'
    xmlns:Manifest = 'http://www.w3.org/2001/XMLSchema-instance'
    xmlns = 'HTTPS://Addons.FreeCAD.Org/Manifest'
>
```

<br/>

<!----------------------------------------------------------------------------->

### 📖 Examples

The following manifests demonstrate  
different configurations you may use.

| File | Contents |
|:-----|:--------|
| [`Everything.xml`] | Manifest with all available elements & attributes.

<br/>

<!----------------------------------------------------------------------------->

## 📑 Repository

| Folder | Purpose |
|:-------|:--------|
| `Source`  | Tree of bite sized XSD source files.
| `Scripts` | Python script used to create a bundle.
| `Assets` | Examples & images used in the docs.
| `.github`  | Configuration & information of the repo.
| `.build`  | Output folder for the bundled schema.

<br/>

<!----------------------------------------------------------------------------->

## 🔧 Development

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

### 📦 Bundling

To bundle the `/Source/` files into a combined schema,  
you just have to run the following Python command:

```sh
python Scripts/Bundle.py
```

This will create a bundled file at `.build/Schema.xsd`

```xml
<?xml-model
    href = '/Path-To-Cloned-Repository/.build/Schema.xsd'
?>
<package
    xmlns = 'HTTPS://Addons.FreeCAD.Org/Manifest'
>
```

<!----------------------------------------------------------------------------->

#### 📜 Preview

[![Bundler Showcase 1]](#)

<br/>

<!----------------------------------------------------------------------------->

## 📋 Versioning

This schema uses semantic versioning with  
2 numbers where the first is the manifest  
format & the second is this schema's build.

`<Manifest Format>.<Schema Build>`

*The [Releases][GitHub Releases] page lists all published versions.*

<br/>

<!----------------------------------------------------------------------------->

## 🚧 Workarounds

Due to the missing [**XSD 1.1 Support**][Support] in the RedHat  
VSCode extension, multiple workarounds are being  
used to approximate the actual schema structure.

-   In XSD 1.1, the `<all>` tag allows for `unbound` elements, the two possible  
    workarounds are using a `sequence` and forcing the order of elements or  
    using `<choice>` and allowing multiple of every tags.

    The `<package>` tag uses the latter to facilitate `<maintainer>` & `<url>`

-   The `<url>` tag should require a `branch` attribute if the  
    `type` attribute was set to `repository`, however currently  
    the `branch` attribute will always be present & optional.

<!----------------------------------------------------------------------------->

[Button Contribute]: https://img.shields.io/badge/Contribute-3D8DDF?style=for-the-badge
[Button Discord]: https://img.shields.io/badge/Discord-5561EC?style=for-the-badge
[Button Website]: https://img.shields.io/badge/Website-E24329?style=for-the-badge

[FreeCAD Addon Manifest]: https://wiki.freecad.org/Package_Metadata
[GitHub Releases]: https://github.com/FreeCAD/FreeCAD-Addon-Manifest-Schema/releases
[Support]: https://github.com/redhat-developer/vscode-xml/issues/222
[Discord]: https://discord.gg/w2cTKGzccC
[Website]: https://freecad.org

[Bundler Showcase 1]: ./Assets/Images/Bundler-Showcase-1.webp
[`Everything.xml`]: ./Assets/Examples/Everything.xml
[Contribute]: ./.github/CONTRIBUTING.md
