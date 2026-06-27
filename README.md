# xna4-spec

Machine-readable XML specification of the **XNA 4.0 API**, converted from the
official Microsoft documentation.

## Purpose

This repository contains a complete description of every XNA 4.0 class, struct,
enum, interface, and delegate — including all properties, methods, constructors,
fields, and events with their original descriptions. It is intended for:

- Auditing C++ reimplementations of XNA 4.0 (comparing what is implemented vs. what is missing)
- Generating API completeness reports
- Serving as a self-contained offline reference without needing the original HTML documentation

## Structure

```
spec/
├── xna.xsd                              # Master XSD schema
├── index.xml                            # Index of all 550 types across 19 namespaces
├── plan.md                              # Conversion plan and task list
├── Microsoft.Xna.Framework/             # Core runtime types
│   ├── Game.xml
│   ├── Vector3.xml
│   └── ...
├── Microsoft.Xna.Framework.Graphics/   # Graphics pipeline types
│   ├── SpriteBatch.xml
│   ├── GraphicsDevice.xml
│   └── ...
└── ...                                  # One directory per namespace
```

## Coverage

| Namespace | Types |
|-----------|-------|
| Microsoft.Xna.Framework | 47 |
| Microsoft.Xna.Framework.Graphics | 175 |
| Microsoft.Xna.Framework.Graphics.PackedVector | 22 |
| Microsoft.Xna.Framework.Audio | 19 |
| Microsoft.Xna.Framework.Input | 17 |
| Microsoft.Xna.Framework.Input.Touch | 8 |
| Microsoft.Xna.Framework.Media | 24 |
| Microsoft.Xna.Framework.Net | 26 |
| Microsoft.Xna.Framework.Storage | 3 |
| Microsoft.Xna.Framework.Content | 12 |
| Microsoft.Xna.Framework.GamerServices | 54 |
| Microsoft.Xna.Framework.Design | 13 |
| Microsoft.Xna.Framework.Content.Pipeline | 32 |
| Microsoft.Xna.Framework.Content.Pipeline.Audio | 5 |
| Microsoft.Xna.Framework.Content.Pipeline.Graphics | 47 |
| Microsoft.Xna.Framework.Content.Pipeline.Processors | 28 |
| Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler | 5 |
| Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate | 7 |
| Microsoft.Xna.Framework.Content.Pipeline.Tasks | 6 |
| **Total** | **550** |

## Source

Converted from the XNA 4.0 HTML documentation originally published at
`learn.microsoft.com/en-us/previous-versions/windows/xna/`.

## Related

- [openeggbert/sharp-runtime](https://github.com/openeggbert/sharp-runtime) — C++ XNA 4.0 reimplementation being audited against this spec
