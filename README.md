<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-ai-600-1

NIST AI RMF - Generative AI Profile - LinkML Schema

See [solution design](./docs/about.md).

## Documentation Website

[https://lmodel.github.io/nist-ai-600-1](https://lmodel.github.io/nist-ai-600-1)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [nist_ai_600_1](src/nist_ai_600_1)
    * [schema/](src/nist_ai_600_1/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/nist_ai_600_1/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/).
To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier).
