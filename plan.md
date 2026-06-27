# XNA 4.0 API Specification — Conversion Plan

## Overview

Convert the downloaded XNA 4.0 HTML documentation (11,473 HTML files) into a
structured, machine-readable `spec/` directory. Each XNA type (class, struct,
enum, interface, delegate) gets its own XML file. The result replaces the HTML
documentation and enables systematic audit of a C++ XNA 4.0 reimplementation.

---

## Source Statistics

- **Total HTML files**: 11,473
- **Unique API types**: 551
  - class: 342
  - struct: 92
  - enum: 101
  - interface: 15
  - delegate: 1
- **Namespaces**: 19

---

## Directory Structure

```
spec/
├── xna.xsd              # T-001: master XSD schema
├── index.xml            # T-002: master type index
├── Microsoft.Xna.Framework/
│   ├── Game.xml
│   ├── Vector3.xml
│   └── ...
├── Microsoft.Xna.Framework.Graphics/
│   ├── SpriteBatch.xml
│   └── ...
└── ...
```

---

## XML Content Per File

Each XML file (`TypeName.xml`) contains the full documentation for one type:
- Summary description
- C# syntax declaration (base class, interfaces)
- Full Remarks text (verbatim from HTML)
- All constructors with parameters and descriptions
- All properties (type, access, description, remarks)
- All methods with all overloads (parameters, return type, description)
- All fields
- All events
- Enum members with descriptions (for enum types)
- Platform availability (Xbox 360, Windows 7/Vista/XP, Windows Phone)

---

## XSD Schema (T-001)

`spec/xna.xsd` defines root elements `<xna-type>` and `<xna-index>` with
complex types: ClassType, StructType, EnumType, InterfaceType, DelegateType,
PropertyDef, MethodDef, OverloadDef, ParameterDef, ConstructorDef, FieldDef,
EventDef, EnumMemberDef, PlatformsDef, SyntaxDef.

---

## Complete Task List

| Task | File | Kind | Namespace |
|------|------|------|-----------|
| T-001 | `xna.xsd` | XSD schema | — |
| T-002 | `index.xml` | XML index | all namespaces |
| | | | **Microsoft.Xna.Framework** |
| T-003 | `Microsoft.Xna.Framework/BoundingBox.xml` | struct | Microsoft.Xna.Framework |
| T-004 | `Microsoft.Xna.Framework/BoundingFrustum.xml` | class | Microsoft.Xna.Framework |
| T-005 | `Microsoft.Xna.Framework/BoundingSphere.xml` | struct | Microsoft.Xna.Framework |
| T-006 | `Microsoft.Xna.Framework/Color.xml` | struct | Microsoft.Xna.Framework |
| T-007 | `Microsoft.Xna.Framework/ContainmentType.xml` | enum | Microsoft.Xna.Framework |
| T-008 | `Microsoft.Xna.Framework/Curve.xml` | class | Microsoft.Xna.Framework |
| T-009 | `Microsoft.Xna.Framework/CurveContinuity.xml` | enum | Microsoft.Xna.Framework |
| T-010 | `Microsoft.Xna.Framework/CurveKey.xml` | class | Microsoft.Xna.Framework |
| T-011 | `Microsoft.Xna.Framework/CurveKeyCollection.xml` | class | Microsoft.Xna.Framework |
| T-012 | `Microsoft.Xna.Framework/CurveLoopType.xml` | enum | Microsoft.Xna.Framework |
| T-013 | `Microsoft.Xna.Framework/CurveTangent.xml` | enum | Microsoft.Xna.Framework |
| T-014 | `Microsoft.Xna.Framework/DisplayOrientation.xml` | enum | Microsoft.Xna.Framework |
| T-015 | `Microsoft.Xna.Framework/DrawableGameComponent.xml` | class | Microsoft.Xna.Framework |
| T-016 | `Microsoft.Xna.Framework/FrameworkDispatcher.xml` | class | Microsoft.Xna.Framework |
| T-017 | `Microsoft.Xna.Framework/Game.xml` | class | Microsoft.Xna.Framework |
| T-018 | `Microsoft.Xna.Framework/GameComponent.xml` | class | Microsoft.Xna.Framework |
| T-019 | `Microsoft.Xna.Framework/GameComponentCollection.xml` | class | Microsoft.Xna.Framework |
| T-020 | `Microsoft.Xna.Framework/GameComponentCollectionEventArgs.xml` | class | Microsoft.Xna.Framework |
| T-021 | `Microsoft.Xna.Framework/GameServiceContainer.xml` | class | Microsoft.Xna.Framework |
| T-022 | `Microsoft.Xna.Framework/GameTime.xml` | class | Microsoft.Xna.Framework |
| T-023 | `Microsoft.Xna.Framework/GameTimer.xml` | class | Microsoft.Xna.Framework |
| T-024 | `Microsoft.Xna.Framework/GameTimerEventArgs.xml` | class | Microsoft.Xna.Framework |
| T-025 | `Microsoft.Xna.Framework/GameWindow.xml` | class | Microsoft.Xna.Framework |
| T-026 | `Microsoft.Xna.Framework/GraphicsDeviceInformation.xml` | class | Microsoft.Xna.Framework |
| T-027 | `Microsoft.Xna.Framework/GraphicsDeviceManager.xml` | class | Microsoft.Xna.Framework |
| T-028 | `Microsoft.Xna.Framework/IDrawable.xml` | interface | Microsoft.Xna.Framework |
| T-029 | `Microsoft.Xna.Framework/IGameComponent.xml` | interface | Microsoft.Xna.Framework |
| T-030 | `Microsoft.Xna.Framework/IGraphicsDeviceManager.xml` | interface | Microsoft.Xna.Framework |
| T-031 | `Microsoft.Xna.Framework/IUpdateable.xml` | interface | Microsoft.Xna.Framework |
| T-032 | `Microsoft.Xna.Framework/LaunchParameters.xml` | class | Microsoft.Xna.Framework |
| T-033 | `Microsoft.Xna.Framework/MathHelper.xml` | class | Microsoft.Xna.Framework |
| T-034 | `Microsoft.Xna.Framework/Matrix.xml` | struct | Microsoft.Xna.Framework |
| T-035 | `Microsoft.Xna.Framework/NoSuitableGraphicsDeviceException.xml` | class | Microsoft.Xna.Framework |
| T-036 | `Microsoft.Xna.Framework/Plane.xml` | struct | Microsoft.Xna.Framework |
| T-037 | `Microsoft.Xna.Framework/PlaneIntersectionType.xml` | enum | Microsoft.Xna.Framework |
| T-038 | `Microsoft.Xna.Framework/PlayerIndex.xml` | enum | Microsoft.Xna.Framework |
| T-039 | `Microsoft.Xna.Framework/Point.xml` | struct | Microsoft.Xna.Framework |
| T-040 | `Microsoft.Xna.Framework/PreparingDeviceSettingsEventArgs.xml` | class | Microsoft.Xna.Framework |
| T-041 | `Microsoft.Xna.Framework/Quaternion.xml` | struct | Microsoft.Xna.Framework |
| T-042 | `Microsoft.Xna.Framework/Ray.xml` | struct | Microsoft.Xna.Framework |
| T-043 | `Microsoft.Xna.Framework/Rectangle.xml` | struct | Microsoft.Xna.Framework |
| T-044 | `Microsoft.Xna.Framework/SharedGraphicsDeviceManager.xml` | class | Microsoft.Xna.Framework |
| T-045 | `Microsoft.Xna.Framework/TargetPlatform.xml` | enum | Microsoft.Xna.Framework |
| T-046 | `Microsoft.Xna.Framework/TitleContainer.xml` | class | Microsoft.Xna.Framework |
| T-047 | `Microsoft.Xna.Framework/Vector2.xml` | struct | Microsoft.Xna.Framework |
| T-048 | `Microsoft.Xna.Framework/Vector3.xml` | struct | Microsoft.Xna.Framework |
| T-049 | `Microsoft.Xna.Framework/Vector4.xml` | struct | Microsoft.Xna.Framework |
| | | | **Microsoft.Xna.Framework.Graphics** |
| T-050 | `Microsoft.Xna.Framework.Graphics/AlphaTestEffect.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-051 | `Microsoft.Xna.Framework.Graphics/BasicDirectionalLight.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-052 | `Microsoft.Xna.Framework.Graphics/BasicEffect.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-053 | `Microsoft.Xna.Framework.Graphics/Blend.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-054 | `Microsoft.Xna.Framework.Graphics/BlendFunction.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-055 | `Microsoft.Xna.Framework.Graphics/BlendState.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-056 | `Microsoft.Xna.Framework.Graphics/BufferUsage.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-057 | `Microsoft.Xna.Framework.Graphics/ClearOptions.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-058 | `Microsoft.Xna.Framework.Graphics/ClipPlane.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-059 | `Microsoft.Xna.Framework.Graphics/ClipPlaneCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-060 | `Microsoft.Xna.Framework.Graphics/Color.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-061 | `Microsoft.Xna.Framework.Graphics/ColorWriteChannels.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-062 | `Microsoft.Xna.Framework.Graphics/CompareFunction.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-063 | `Microsoft.Xna.Framework.Graphics/CompilationFailedException.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-064 | `Microsoft.Xna.Framework.Graphics/CompiledEffect.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-065 | `Microsoft.Xna.Framework.Graphics/CompiledShader.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-066 | `Microsoft.Xna.Framework.Graphics/CompilerIncludeHandler.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-067 | `Microsoft.Xna.Framework.Graphics/CompilerIncludeHandlerType.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-068 | `Microsoft.Xna.Framework.Graphics/CompilerMacro.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-069 | `Microsoft.Xna.Framework.Graphics/CompilerOptions.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-070 | `Microsoft.Xna.Framework.Graphics/CreateOptions.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-071 | `Microsoft.Xna.Framework.Graphics/CubeMapFace.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-072 | `Microsoft.Xna.Framework.Graphics/CullMode.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-073 | `Microsoft.Xna.Framework.Graphics/DepthFormat.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-074 | `Microsoft.Xna.Framework.Graphics/DepthStencilBuffer.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-075 | `Microsoft.Xna.Framework.Graphics/DepthStencilState.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-076 | `Microsoft.Xna.Framework.Graphics/DeviceLostException.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-077 | `Microsoft.Xna.Framework.Graphics/DeviceNotResetException.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-078 | `Microsoft.Xna.Framework.Graphics/DeviceNotSupportedException.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-079 | `Microsoft.Xna.Framework.Graphics/DeviceStillDrawingException.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-080 | `Microsoft.Xna.Framework.Graphics/DeviceType.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-081 | `Microsoft.Xna.Framework.Graphics/DirectionalLight.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-082 | `Microsoft.Xna.Framework.Graphics/DisplayMode.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-083 | `Microsoft.Xna.Framework.Graphics/DisplayModeCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-084 | `Microsoft.Xna.Framework.Graphics/DriverInternalErrorException.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-085 | `Microsoft.Xna.Framework.Graphics/DualTextureEffect.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-086 | `Microsoft.Xna.Framework.Graphics/DynamicIndexBuffer.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-087 | `Microsoft.Xna.Framework.Graphics/DynamicVertexBuffer.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-088 | `Microsoft.Xna.Framework.Graphics/Effect.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-089 | `Microsoft.Xna.Framework.Graphics/EffectAnnotation.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-090 | `Microsoft.Xna.Framework.Graphics/EffectAnnotationCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-091 | `Microsoft.Xna.Framework.Graphics/EffectFunction.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-092 | `Microsoft.Xna.Framework.Graphics/EffectFunctionCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-093 | `Microsoft.Xna.Framework.Graphics/EffectMaterial.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-094 | `Microsoft.Xna.Framework.Graphics/EffectParameter.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-095 | `Microsoft.Xna.Framework.Graphics/EffectParameterBlock.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-096 | `Microsoft.Xna.Framework.Graphics/EffectParameterClass.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-097 | `Microsoft.Xna.Framework.Graphics/EffectParameterCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-098 | `Microsoft.Xna.Framework.Graphics/EffectParameterType.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-099 | `Microsoft.Xna.Framework.Graphics/EffectPass.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-100 | `Microsoft.Xna.Framework.Graphics/EffectPassCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-101 | `Microsoft.Xna.Framework.Graphics/EffectPool.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-102 | `Microsoft.Xna.Framework.Graphics/EffectTechnique.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-103 | `Microsoft.Xna.Framework.Graphics/EffectTechniqueCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-104 | `Microsoft.Xna.Framework.Graphics/EnvironmentMapEffect.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-105 | `Microsoft.Xna.Framework.Graphics/FillMode.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-106 | `Microsoft.Xna.Framework.Graphics/FilterOptions.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-107 | `Microsoft.Xna.Framework.Graphics/FogMode.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-108 | `Microsoft.Xna.Framework.Graphics/GammaRamp.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-109 | `Microsoft.Xna.Framework.Graphics/GraphicsAdapter.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-110 | `Microsoft.Xna.Framework.Graphics/GraphicsDevice.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-111 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-112 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.AddressCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-113 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.BlendCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-114 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.CompareCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-115 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.CursorCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-116 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.DeclarationTypeCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-117 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.DeviceCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-118 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.DriverCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-119 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.FilterCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-120 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.LineCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-121 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.PixelShaderCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-122 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.PrimitiveCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-123 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.RasterCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-124 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.ShadingCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-125 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.StencilCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-126 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.TextureCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-127 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.VertexFormatCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-128 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.VertexProcessingCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-129 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCapabilities.VertexShaderCaps.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-130 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceCreationParameters.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-131 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceExtensions.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-132 | `Microsoft.Xna.Framework.Graphics/GraphicsDeviceStatus.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-133 | `Microsoft.Xna.Framework.Graphics/GraphicsProfile.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-134 | `Microsoft.Xna.Framework.Graphics/GraphicsResource.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-135 | `Microsoft.Xna.Framework.Graphics/IEffectFog.xml` | interface | Microsoft.Xna.Framework.Graphics |
| T-136 | `Microsoft.Xna.Framework.Graphics/IEffectLights.xml` | interface | Microsoft.Xna.Framework.Graphics |
| T-137 | `Microsoft.Xna.Framework.Graphics/IEffectMatrices.xml` | interface | Microsoft.Xna.Framework.Graphics |
| T-138 | `Microsoft.Xna.Framework.Graphics/IGraphicsDeviceService.xml` | interface | Microsoft.Xna.Framework.Graphics |
| T-139 | `Microsoft.Xna.Framework.Graphics/IVertexType.xml` | interface | Microsoft.Xna.Framework.Graphics |
| T-140 | `Microsoft.Xna.Framework.Graphics/ImageFileFormat.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-141 | `Microsoft.Xna.Framework.Graphics/IndexBuffer.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-142 | `Microsoft.Xna.Framework.Graphics/IndexElementSize.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-143 | `Microsoft.Xna.Framework.Graphics/Model.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-144 | `Microsoft.Xna.Framework.Graphics/ModelBone.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-145 | `Microsoft.Xna.Framework.Graphics/ModelBoneCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-146 | `Microsoft.Xna.Framework.Graphics/ModelBoneCollection.Enumerator.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-147 | `Microsoft.Xna.Framework.Graphics/ModelEffectCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-148 | `Microsoft.Xna.Framework.Graphics/ModelEffectCollection.Enumerator.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-149 | `Microsoft.Xna.Framework.Graphics/ModelMesh.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-150 | `Microsoft.Xna.Framework.Graphics/ModelMeshCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-151 | `Microsoft.Xna.Framework.Graphics/ModelMeshCollection.Enumerator.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-152 | `Microsoft.Xna.Framework.Graphics/ModelMeshPart.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-153 | `Microsoft.Xna.Framework.Graphics/ModelMeshPartCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-154 | `Microsoft.Xna.Framework.Graphics/ModelMeshPartCollection.Enumerator.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-155 | `Microsoft.Xna.Framework.Graphics/MultiSampleType.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-156 | `Microsoft.Xna.Framework.Graphics/NoSuitableGraphicsDeviceException.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-157 | `Microsoft.Xna.Framework.Graphics/OcclusionQuery.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-158 | `Microsoft.Xna.Framework.Graphics/OutOfVideoMemoryException.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-159 | `Microsoft.Xna.Framework.Graphics/PixelShader.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-160 | `Microsoft.Xna.Framework.Graphics/PresentInterval.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-161 | `Microsoft.Xna.Framework.Graphics/PresentOptions.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-162 | `Microsoft.Xna.Framework.Graphics/PresentationParameters.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-163 | `Microsoft.Xna.Framework.Graphics/PrimitiveType.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-164 | `Microsoft.Xna.Framework.Graphics/QueryUsages.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-165 | `Microsoft.Xna.Framework.Graphics/RasterStatus.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-166 | `Microsoft.Xna.Framework.Graphics/RasterizerState.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-167 | `Microsoft.Xna.Framework.Graphics/RenderState.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-168 | `Microsoft.Xna.Framework.Graphics/RenderTarget.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-169 | `Microsoft.Xna.Framework.Graphics/RenderTarget2D.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-170 | `Microsoft.Xna.Framework.Graphics/RenderTargetBinding.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-171 | `Microsoft.Xna.Framework.Graphics/RenderTargetCube.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-172 | `Microsoft.Xna.Framework.Graphics/RenderTargetUsage.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-173 | `Microsoft.Xna.Framework.Graphics/ResourceCreatedEventArgs.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-174 | `Microsoft.Xna.Framework.Graphics/ResourceDestroyedEventArgs.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-175 | `Microsoft.Xna.Framework.Graphics/ResourceManagementMode.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-176 | `Microsoft.Xna.Framework.Graphics/ResourceType.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-177 | `Microsoft.Xna.Framework.Graphics/ResourceUsage.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-178 | `Microsoft.Xna.Framework.Graphics/SamplerState.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-179 | `Microsoft.Xna.Framework.Graphics/SamplerStateCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-180 | `Microsoft.Xna.Framework.Graphics/SaveStateMode.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-181 | `Microsoft.Xna.Framework.Graphics/SetDataOptions.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-182 | `Microsoft.Xna.Framework.Graphics/ShaderCompiler.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-183 | `Microsoft.Xna.Framework.Graphics/ShaderConstant.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-184 | `Microsoft.Xna.Framework.Graphics/ShaderConstantCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-185 | `Microsoft.Xna.Framework.Graphics/ShaderConstantTable.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-186 | `Microsoft.Xna.Framework.Graphics/ShaderProfile.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-187 | `Microsoft.Xna.Framework.Graphics/ShaderRegisterSet.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-188 | `Microsoft.Xna.Framework.Graphics/ShaderSemantic.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-189 | `Microsoft.Xna.Framework.Graphics/SkinnedEffect.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-190 | `Microsoft.Xna.Framework.Graphics/SpriteBatch.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-191 | `Microsoft.Xna.Framework.Graphics/SpriteBlendMode.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-192 | `Microsoft.Xna.Framework.Graphics/SpriteEffects.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-193 | `Microsoft.Xna.Framework.Graphics/SpriteFont.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-194 | `Microsoft.Xna.Framework.Graphics/SpriteSortMode.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-195 | `Microsoft.Xna.Framework.Graphics/StateBlock.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-196 | `Microsoft.Xna.Framework.Graphics/StencilOperation.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-197 | `Microsoft.Xna.Framework.Graphics/SurfaceFormat.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-198 | `Microsoft.Xna.Framework.Graphics/SwapEffect.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-199 | `Microsoft.Xna.Framework.Graphics/Texture.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-200 | `Microsoft.Xna.Framework.Graphics/Texture2D.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-201 | `Microsoft.Xna.Framework.Graphics/Texture3D.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-202 | `Microsoft.Xna.Framework.Graphics/TextureAddressMode.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-203 | `Microsoft.Xna.Framework.Graphics/TextureCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-204 | `Microsoft.Xna.Framework.Graphics/TextureCreationParameters.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-205 | `Microsoft.Xna.Framework.Graphics/TextureCube.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-206 | `Microsoft.Xna.Framework.Graphics/TextureFilter.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-207 | `Microsoft.Xna.Framework.Graphics/TextureInformation.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-208 | `Microsoft.Xna.Framework.Graphics/TextureUsage.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-209 | `Microsoft.Xna.Framework.Graphics/TextureWrapCoordinates.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-210 | `Microsoft.Xna.Framework.Graphics/UIElementRenderer.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-211 | `Microsoft.Xna.Framework.Graphics/VertexBuffer.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-212 | `Microsoft.Xna.Framework.Graphics/VertexBufferBinding.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-213 | `Microsoft.Xna.Framework.Graphics/VertexDeclaration.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-214 | `Microsoft.Xna.Framework.Graphics/VertexElement.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-215 | `Microsoft.Xna.Framework.Graphics/VertexElementFormat.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-216 | `Microsoft.Xna.Framework.Graphics/VertexElementMethod.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-217 | `Microsoft.Xna.Framework.Graphics/VertexElementUsage.xml` | enum | Microsoft.Xna.Framework.Graphics |
| T-218 | `Microsoft.Xna.Framework.Graphics/VertexPositionColor.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-219 | `Microsoft.Xna.Framework.Graphics/VertexPositionColorTexture.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-220 | `Microsoft.Xna.Framework.Graphics/VertexPositionNormalTexture.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-221 | `Microsoft.Xna.Framework.Graphics/VertexPositionTexture.xml` | struct | Microsoft.Xna.Framework.Graphics |
| T-222 | `Microsoft.Xna.Framework.Graphics/VertexShader.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-223 | `Microsoft.Xna.Framework.Graphics/VertexStream.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-224 | `Microsoft.Xna.Framework.Graphics/VertexStreamCollection.xml` | class | Microsoft.Xna.Framework.Graphics |
| T-225 | `Microsoft.Xna.Framework.Graphics/Viewport.xml` | struct | Microsoft.Xna.Framework.Graphics |
| | | | **Microsoft.Xna.Framework.Graphics.PackedVector** |
| T-226 | `Microsoft.Xna.Framework.Graphics.PackedVector/Alpha8.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-227 | `Microsoft.Xna.Framework.Graphics.PackedVector/Bgr565.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-228 | `Microsoft.Xna.Framework.Graphics.PackedVector/Bgra4444.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-229 | `Microsoft.Xna.Framework.Graphics.PackedVector/Bgra5551.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-230 | `Microsoft.Xna.Framework.Graphics.PackedVector/Byte4.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-231 | `Microsoft.Xna.Framework.Graphics.PackedVector/HalfSingle.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-232 | `Microsoft.Xna.Framework.Graphics.PackedVector/HalfVector2.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-233 | `Microsoft.Xna.Framework.Graphics.PackedVector/HalfVector4.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-234 | `Microsoft.Xna.Framework.Graphics.PackedVector/IPackedVector.xml` | interface | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-235 | `Microsoft.Xna.Framework.Graphics.PackedVector/IPackedVector Generic.xml` | interface | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-236 | `Microsoft.Xna.Framework.Graphics.PackedVector/Normalized101010.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-237 | `Microsoft.Xna.Framework.Graphics.PackedVector/NormalizedByte2.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-238 | `Microsoft.Xna.Framework.Graphics.PackedVector/NormalizedByte4.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-239 | `Microsoft.Xna.Framework.Graphics.PackedVector/NormalizedShort2.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-240 | `Microsoft.Xna.Framework.Graphics.PackedVector/NormalizedShort4.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-241 | `Microsoft.Xna.Framework.Graphics.PackedVector/Rg32.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-242 | `Microsoft.Xna.Framework.Graphics.PackedVector/Rgba1010102.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-243 | `Microsoft.Xna.Framework.Graphics.PackedVector/Rgba32.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-244 | `Microsoft.Xna.Framework.Graphics.PackedVector/Rgba64.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-245 | `Microsoft.Xna.Framework.Graphics.PackedVector/Short2.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-246 | `Microsoft.Xna.Framework.Graphics.PackedVector/Short4.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| T-247 | `Microsoft.Xna.Framework.Graphics.PackedVector/UInt101010.xml` | struct | Microsoft.Xna.Framework.Graphics.PackedVector |
| | | | **Microsoft.Xna.Framework.Audio** |
| T-248 | `Microsoft.Xna.Framework.Audio/AudioCategory.xml` | struct | Microsoft.Xna.Framework.Audio |
| T-249 | `Microsoft.Xna.Framework.Audio/AudioChannels.xml` | enum | Microsoft.Xna.Framework.Audio |
| T-250 | `Microsoft.Xna.Framework.Audio/AudioEmitter.xml` | class | Microsoft.Xna.Framework.Audio |
| T-251 | `Microsoft.Xna.Framework.Audio/AudioEngine.xml` | class | Microsoft.Xna.Framework.Audio |
| T-252 | `Microsoft.Xna.Framework.Audio/AudioListener.xml` | class | Microsoft.Xna.Framework.Audio |
| T-253 | `Microsoft.Xna.Framework.Audio/AudioStopOptions.xml` | enum | Microsoft.Xna.Framework.Audio |
| T-254 | `Microsoft.Xna.Framework.Audio/Cue.xml` | class | Microsoft.Xna.Framework.Audio |
| T-255 | `Microsoft.Xna.Framework.Audio/DynamicSoundEffectInstance.xml` | class | Microsoft.Xna.Framework.Audio |
| T-256 | `Microsoft.Xna.Framework.Audio/InstancePlayLimitException.xml` | class | Microsoft.Xna.Framework.Audio |
| T-257 | `Microsoft.Xna.Framework.Audio/Microphone.xml` | class | Microsoft.Xna.Framework.Audio |
| T-258 | `Microsoft.Xna.Framework.Audio/MicrophoneState.xml` | enum | Microsoft.Xna.Framework.Audio |
| T-259 | `Microsoft.Xna.Framework.Audio/NoAudioHardwareException.xml` | class | Microsoft.Xna.Framework.Audio |
| T-260 | `Microsoft.Xna.Framework.Audio/NoMicrophoneConnectedException.xml` | class | Microsoft.Xna.Framework.Audio |
| T-261 | `Microsoft.Xna.Framework.Audio/RendererDetail.xml` | struct | Microsoft.Xna.Framework.Audio |
| T-262 | `Microsoft.Xna.Framework.Audio/SoundBank.xml` | class | Microsoft.Xna.Framework.Audio |
| T-263 | `Microsoft.Xna.Framework.Audio/SoundEffect.xml` | class | Microsoft.Xna.Framework.Audio |
| T-264 | `Microsoft.Xna.Framework.Audio/SoundEffectInstance.xml` | class | Microsoft.Xna.Framework.Audio |
| T-265 | `Microsoft.Xna.Framework.Audio/SoundState.xml` | enum | Microsoft.Xna.Framework.Audio |
| T-266 | `Microsoft.Xna.Framework.Audio/WaveBank.xml` | class | Microsoft.Xna.Framework.Audio |
| | | | **Microsoft.Xna.Framework.Input** |
| T-267 | `Microsoft.Xna.Framework.Input/ButtonState.xml` | enum | Microsoft.Xna.Framework.Input |
| T-268 | `Microsoft.Xna.Framework.Input/Buttons.xml` | enum | Microsoft.Xna.Framework.Input |
| T-269 | `Microsoft.Xna.Framework.Input/GamePad.xml` | class | Microsoft.Xna.Framework.Input |
| T-270 | `Microsoft.Xna.Framework.Input/GamePadButtons.xml` | struct | Microsoft.Xna.Framework.Input |
| T-271 | `Microsoft.Xna.Framework.Input/GamePadCapabilities.xml` | struct | Microsoft.Xna.Framework.Input |
| T-272 | `Microsoft.Xna.Framework.Input/GamePadDPad.xml` | struct | Microsoft.Xna.Framework.Input |
| T-273 | `Microsoft.Xna.Framework.Input/GamePadDeadZone.xml` | enum | Microsoft.Xna.Framework.Input |
| T-274 | `Microsoft.Xna.Framework.Input/GamePadState.xml` | struct | Microsoft.Xna.Framework.Input |
| T-275 | `Microsoft.Xna.Framework.Input/GamePadThumbSticks.xml` | struct | Microsoft.Xna.Framework.Input |
| T-276 | `Microsoft.Xna.Framework.Input/GamePadTriggers.xml` | struct | Microsoft.Xna.Framework.Input |
| T-277 | `Microsoft.Xna.Framework.Input/GamePadType.xml` | enum | Microsoft.Xna.Framework.Input |
| T-278 | `Microsoft.Xna.Framework.Input/KeyState.xml` | enum | Microsoft.Xna.Framework.Input |
| T-279 | `Microsoft.Xna.Framework.Input/Keyboard.xml` | class | Microsoft.Xna.Framework.Input |
| T-280 | `Microsoft.Xna.Framework.Input/KeyboardState.xml` | struct | Microsoft.Xna.Framework.Input |
| T-281 | `Microsoft.Xna.Framework.Input/Keys.xml` | enum | Microsoft.Xna.Framework.Input |
| T-282 | `Microsoft.Xna.Framework.Input/Mouse.xml` | class | Microsoft.Xna.Framework.Input |
| T-283 | `Microsoft.Xna.Framework.Input/MouseState.xml` | struct | Microsoft.Xna.Framework.Input |
| | | | **Microsoft.Xna.Framework.Input.Touch** |
| T-284 | `Microsoft.Xna.Framework.Input.Touch/GestureSample.xml` | struct | Microsoft.Xna.Framework.Input.Touch |
| T-285 | `Microsoft.Xna.Framework.Input.Touch/GestureType.xml` | enum | Microsoft.Xna.Framework.Input.Touch |
| T-286 | `Microsoft.Xna.Framework.Input.Touch/TouchCollection.xml` | struct | Microsoft.Xna.Framework.Input.Touch |
| T-287 | `Microsoft.Xna.Framework.Input.Touch/TouchCollection.Enumerator.xml` | struct | Microsoft.Xna.Framework.Input.Touch |
| T-288 | `Microsoft.Xna.Framework.Input.Touch/TouchLocation.xml` | struct | Microsoft.Xna.Framework.Input.Touch |
| T-289 | `Microsoft.Xna.Framework.Input.Touch/TouchLocationState.xml` | enum | Microsoft.Xna.Framework.Input.Touch |
| T-290 | `Microsoft.Xna.Framework.Input.Touch/TouchPanel.xml` | class | Microsoft.Xna.Framework.Input.Touch |
| T-291 | `Microsoft.Xna.Framework.Input.Touch/TouchPanelCapabilities.xml` | struct | Microsoft.Xna.Framework.Input.Touch |
| | | | **Microsoft.Xna.Framework.Media** |
| T-292 | `Microsoft.Xna.Framework.Media/Album.xml` | class | Microsoft.Xna.Framework.Media |
| T-293 | `Microsoft.Xna.Framework.Media/AlbumCollection.xml` | class | Microsoft.Xna.Framework.Media |
| T-294 | `Microsoft.Xna.Framework.Media/Artist.xml` | class | Microsoft.Xna.Framework.Media |
| T-295 | `Microsoft.Xna.Framework.Media/ArtistCollection.xml` | class | Microsoft.Xna.Framework.Media |
| T-296 | `Microsoft.Xna.Framework.Media/Genre.xml` | class | Microsoft.Xna.Framework.Media |
| T-297 | `Microsoft.Xna.Framework.Media/GenreCollection.xml` | class | Microsoft.Xna.Framework.Media |
| T-298 | `Microsoft.Xna.Framework.Media/MediaLibrary.xml` | class | Microsoft.Xna.Framework.Media |
| T-299 | `Microsoft.Xna.Framework.Media/MediaPlayer.xml` | class | Microsoft.Xna.Framework.Media |
| T-300 | `Microsoft.Xna.Framework.Media/MediaQueue.xml` | class | Microsoft.Xna.Framework.Media |
| T-301 | `Microsoft.Xna.Framework.Media/MediaSource.xml` | class | Microsoft.Xna.Framework.Media |
| T-302 | `Microsoft.Xna.Framework.Media/MediaSourceType.xml` | enum | Microsoft.Xna.Framework.Media |
| T-303 | `Microsoft.Xna.Framework.Media/MediaState.xml` | enum | Microsoft.Xna.Framework.Media |
| T-304 | `Microsoft.Xna.Framework.Media/Picture.xml` | class | Microsoft.Xna.Framework.Media |
| T-305 | `Microsoft.Xna.Framework.Media/PictureAlbum.xml` | class | Microsoft.Xna.Framework.Media |
| T-306 | `Microsoft.Xna.Framework.Media/PictureAlbumCollection.xml` | class | Microsoft.Xna.Framework.Media |
| T-307 | `Microsoft.Xna.Framework.Media/PictureCollection.xml` | class | Microsoft.Xna.Framework.Media |
| T-308 | `Microsoft.Xna.Framework.Media/Playlist.xml` | class | Microsoft.Xna.Framework.Media |
| T-309 | `Microsoft.Xna.Framework.Media/PlaylistCollection.xml` | class | Microsoft.Xna.Framework.Media |
| T-310 | `Microsoft.Xna.Framework.Media/Song.xml` | class | Microsoft.Xna.Framework.Media |
| T-311 | `Microsoft.Xna.Framework.Media/SongCollection.xml` | class | Microsoft.Xna.Framework.Media |
| T-312 | `Microsoft.Xna.Framework.Media/Video.xml` | class | Microsoft.Xna.Framework.Media |
| T-313 | `Microsoft.Xna.Framework.Media/VideoPlayer.xml` | class | Microsoft.Xna.Framework.Media |
| T-314 | `Microsoft.Xna.Framework.Media/VideoSoundtrackType.xml` | enum | Microsoft.Xna.Framework.Media |
| T-315 | `Microsoft.Xna.Framework.Media/VisualizationData.xml` | class | Microsoft.Xna.Framework.Media |
| | | | **Microsoft.Xna.Framework.Net** |
| T-316 | `Microsoft.Xna.Framework.Net/AvailableNetworkSession.xml` | class | Microsoft.Xna.Framework.Net |
| T-317 | `Microsoft.Xna.Framework.Net/AvailableNetworkSessionCollection.xml` | class | Microsoft.Xna.Framework.Net |
| T-318 | `Microsoft.Xna.Framework.Net/GameEndedEventArgs.xml` | class | Microsoft.Xna.Framework.Net |
| T-319 | `Microsoft.Xna.Framework.Net/GameStartedEventArgs.xml` | class | Microsoft.Xna.Framework.Net |
| T-320 | `Microsoft.Xna.Framework.Net/GamerJoinedEventArgs.xml` | class | Microsoft.Xna.Framework.Net |
| T-321 | `Microsoft.Xna.Framework.Net/GamerLeftEventArgs.xml` | class | Microsoft.Xna.Framework.Net |
| T-322 | `Microsoft.Xna.Framework.Net/HostChangedEventArgs.xml` | class | Microsoft.Xna.Framework.Net |
| T-323 | `Microsoft.Xna.Framework.Net/InviteAcceptedEventArgs.xml` | class | Microsoft.Xna.Framework.Net |
| T-324 | `Microsoft.Xna.Framework.Net/LocalNetworkGamer.xml` | class | Microsoft.Xna.Framework.Net |
| T-325 | `Microsoft.Xna.Framework.Net/NetworkException.xml` | class | Microsoft.Xna.Framework.Net |
| T-326 | `Microsoft.Xna.Framework.Net/NetworkGamer.xml` | class | Microsoft.Xna.Framework.Net |
| T-327 | `Microsoft.Xna.Framework.Net/NetworkMachine.xml` | class | Microsoft.Xna.Framework.Net |
| T-328 | `Microsoft.Xna.Framework.Net/NetworkNotAvailableException.xml` | class | Microsoft.Xna.Framework.Net |
| T-329 | `Microsoft.Xna.Framework.Net/NetworkSession.xml` | class | Microsoft.Xna.Framework.Net |
| T-330 | `Microsoft.Xna.Framework.Net/NetworkSessionEndReason.xml` | enum | Microsoft.Xna.Framework.Net |
| T-331 | `Microsoft.Xna.Framework.Net/NetworkSessionEndedEventArgs.xml` | class | Microsoft.Xna.Framework.Net |
| T-332 | `Microsoft.Xna.Framework.Net/NetworkSessionJoinError.xml` | enum | Microsoft.Xna.Framework.Net |
| T-333 | `Microsoft.Xna.Framework.Net/NetworkSessionJoinException.xml` | class | Microsoft.Xna.Framework.Net |
| T-334 | `Microsoft.Xna.Framework.Net/NetworkSessionProperties.xml` | class | Microsoft.Xna.Framework.Net |
| T-335 | `Microsoft.Xna.Framework.Net/NetworkSessionState.xml` | enum | Microsoft.Xna.Framework.Net |
| T-336 | `Microsoft.Xna.Framework.Net/NetworkSessionType.xml` | enum | Microsoft.Xna.Framework.Net |
| T-337 | `Microsoft.Xna.Framework.Net/PacketReader.xml` | class | Microsoft.Xna.Framework.Net |
| T-338 | `Microsoft.Xna.Framework.Net/PacketWriter.xml` | class | Microsoft.Xna.Framework.Net |
| T-339 | `Microsoft.Xna.Framework.Net/QualityOfService.xml` | class | Microsoft.Xna.Framework.Net |
| T-340 | `Microsoft.Xna.Framework.Net/SendDataOptions.xml` | enum | Microsoft.Xna.Framework.Net |
| T-341 | `Microsoft.Xna.Framework.Net/WriteLeaderboardsEventArgs.xml` | class | Microsoft.Xna.Framework.Net |
| | | | **Microsoft.Xna.Framework.Storage** |
| T-342 | `Microsoft.Xna.Framework.Storage/StorageContainer.xml` | class | Microsoft.Xna.Framework.Storage |
| T-343 | `Microsoft.Xna.Framework.Storage/StorageDevice.xml` | class | Microsoft.Xna.Framework.Storage |
| T-344 | `Microsoft.Xna.Framework.Storage/StorageDeviceNotConnectedException.xml` | class | Microsoft.Xna.Framework.Storage |
| | | | **Microsoft.Xna.Framework.Content** |
| T-345 | `Microsoft.Xna.Framework.Content/ContentLoadException.xml` | class | Microsoft.Xna.Framework.Content |
| T-346 | `Microsoft.Xna.Framework.Content/ContentManager.xml` | class | Microsoft.Xna.Framework.Content |
| T-347 | `Microsoft.Xna.Framework.Content/ContentReader.xml` | class | Microsoft.Xna.Framework.Content |
| T-348 | `Microsoft.Xna.Framework.Content/ContentSerializerAttribute.xml` | class | Microsoft.Xna.Framework.Content |
| T-349 | `Microsoft.Xna.Framework.Content/ContentSerializerCollectionItemNameAttribute.xml` | class | Microsoft.Xna.Framework.Content |
| T-350 | `Microsoft.Xna.Framework.Content/ContentSerializerIgnoreAttribute.xml` | class | Microsoft.Xna.Framework.Content |
| T-351 | `Microsoft.Xna.Framework.Content/ContentSerializerRuntimeTypeAttribute.xml` | class | Microsoft.Xna.Framework.Content |
| T-352 | `Microsoft.Xna.Framework.Content/ContentSerializerTypeVersionAttribute.xml` | class | Microsoft.Xna.Framework.Content |
| T-353 | `Microsoft.Xna.Framework.Content/ContentTypeReader.xml` | class | Microsoft.Xna.Framework.Content |
| T-354 | `Microsoft.Xna.Framework.Content/ContentTypeReader Generic.xml` | class | Microsoft.Xna.Framework.Content |
| T-355 | `Microsoft.Xna.Framework.Content/ContentTypeReaderManager.xml` | class | Microsoft.Xna.Framework.Content |
| T-356 | `Microsoft.Xna.Framework.Content/ResourceContentManager.xml` | class | Microsoft.Xna.Framework.Content |
| | | | **Microsoft.Xna.Framework.GamerServices** |
| T-357 | `Microsoft.Xna.Framework.GamerServices/Achievement.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-358 | `Microsoft.Xna.Framework.GamerServices/AchievementCollection.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-359 | `Microsoft.Xna.Framework.GamerServices/AvatarAnimation.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-360 | `Microsoft.Xna.Framework.GamerServices/AvatarAnimationPreset.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-361 | `Microsoft.Xna.Framework.GamerServices/AvatarBodyType.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-362 | `Microsoft.Xna.Framework.GamerServices/AvatarBone.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-363 | `Microsoft.Xna.Framework.GamerServices/AvatarDescription.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-364 | `Microsoft.Xna.Framework.GamerServices/AvatarExpression.xml` | struct | Microsoft.Xna.Framework.GamerServices |
| T-365 | `Microsoft.Xna.Framework.GamerServices/AvatarEye.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-366 | `Microsoft.Xna.Framework.GamerServices/AvatarEyebrow.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-367 | `Microsoft.Xna.Framework.GamerServices/AvatarMouth.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-368 | `Microsoft.Xna.Framework.GamerServices/AvatarRenderer.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-369 | `Microsoft.Xna.Framework.GamerServices/AvatarRendererState.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-370 | `Microsoft.Xna.Framework.GamerServices/ControllerSensitivity.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-371 | `Microsoft.Xna.Framework.GamerServices/FriendCollection.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-372 | `Microsoft.Xna.Framework.GamerServices/FriendGamer.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-373 | `Microsoft.Xna.Framework.GamerServices/GameDefaults.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-374 | `Microsoft.Xna.Framework.GamerServices/GameDifficulty.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-375 | `Microsoft.Xna.Framework.GamerServices/GameUpdateRequiredException.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-376 | `Microsoft.Xna.Framework.GamerServices/Gamer.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-377 | `Microsoft.Xna.Framework.GamerServices/GamerCollection Generic.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-378 | `Microsoft.Xna.Framework.GamerServices/GamerCollection.GamerCollectionEnumerator.xml` | struct | Microsoft.Xna.Framework.GamerServices |
| T-379 | `Microsoft.Xna.Framework.GamerServices/GamerCollection.GamerCollectionEnumerator Generic.xml` | struct | Microsoft.Xna.Framework.GamerServices |
| T-380 | `Microsoft.Xna.Framework.GamerServices/GamerPresence.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-381 | `Microsoft.Xna.Framework.GamerServices/GamerPresenceMode.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-382 | `Microsoft.Xna.Framework.GamerServices/GamerPrivilegeException.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-383 | `Microsoft.Xna.Framework.GamerServices/GamerPrivilegeSetting.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-384 | `Microsoft.Xna.Framework.GamerServices/GamerPrivileges.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-385 | `Microsoft.Xna.Framework.GamerServices/GamerProfile.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-386 | `Microsoft.Xna.Framework.GamerServices/GamerServicesComponent.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-387 | `Microsoft.Xna.Framework.GamerServices/GamerServicesDispatcher.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-388 | `Microsoft.Xna.Framework.GamerServices/GamerServicesNotAvailableException.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-389 | `Microsoft.Xna.Framework.GamerServices/GamerZone.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-390 | `Microsoft.Xna.Framework.GamerServices/Guide.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-391 | `Microsoft.Xna.Framework.GamerServices/GuideAlreadyVisibleException.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-392 | `Microsoft.Xna.Framework.GamerServices/IAvatarAnimation.xml` | interface | Microsoft.Xna.Framework.GamerServices |
| T-393 | `Microsoft.Xna.Framework.GamerServices/InviteAcceptedEventArgs.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-394 | `Microsoft.Xna.Framework.GamerServices/LeaderboardEntry.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-395 | `Microsoft.Xna.Framework.GamerServices/LeaderboardIdentity.xml` | struct | Microsoft.Xna.Framework.GamerServices |
| T-396 | `Microsoft.Xna.Framework.GamerServices/LeaderboardKey.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-397 | `Microsoft.Xna.Framework.GamerServices/LeaderboardOutcome.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-398 | `Microsoft.Xna.Framework.GamerServices/LeaderboardReader.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-399 | `Microsoft.Xna.Framework.GamerServices/LeaderboardWriter.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-400 | `Microsoft.Xna.Framework.GamerServices/MessageBoxIcon.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-401 | `Microsoft.Xna.Framework.GamerServices/NetworkException.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-402 | `Microsoft.Xna.Framework.GamerServices/NetworkNotAvailableException.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-403 | `Microsoft.Xna.Framework.GamerServices/NotificationPosition.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-404 | `Microsoft.Xna.Framework.GamerServices/PropertyDictionary.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-405 | `Microsoft.Xna.Framework.GamerServices/RacingCameraAngle.xml` | enum | Microsoft.Xna.Framework.GamerServices |
| T-406 | `Microsoft.Xna.Framework.GamerServices/SignedInEventArgs.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-407 | `Microsoft.Xna.Framework.GamerServices/SignedInGamer.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-408 | `Microsoft.Xna.Framework.GamerServices/SignedInGamerCollection.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-409 | `Microsoft.Xna.Framework.GamerServices/SignedInGamerExtensions.xml` | class | Microsoft.Xna.Framework.GamerServices |
| T-410 | `Microsoft.Xna.Framework.GamerServices/SignedOutEventArgs.xml` | class | Microsoft.Xna.Framework.GamerServices |
| | | | **Microsoft.Xna.Framework.Design** |
| T-411 | `Microsoft.Xna.Framework.Design/BoundingBoxConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-412 | `Microsoft.Xna.Framework.Design/BoundingSphereConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-413 | `Microsoft.Xna.Framework.Design/ColorConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-414 | `Microsoft.Xna.Framework.Design/MathTypeConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-415 | `Microsoft.Xna.Framework.Design/MatrixConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-416 | `Microsoft.Xna.Framework.Design/PlaneConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-417 | `Microsoft.Xna.Framework.Design/PointConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-418 | `Microsoft.Xna.Framework.Design/QuaternionConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-419 | `Microsoft.Xna.Framework.Design/RayConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-420 | `Microsoft.Xna.Framework.Design/RectangleConverter.xml` | class | Microsoft.Xna.Framework.Design |
| T-421 | `Microsoft.Xna.Framework.Design/Vector2Converter.xml` | class | Microsoft.Xna.Framework.Design |
| T-422 | `Microsoft.Xna.Framework.Design/Vector3Converter.xml` | class | Microsoft.Xna.Framework.Design |
| T-423 | `Microsoft.Xna.Framework.Design/Vector4Converter.xml` | class | Microsoft.Xna.Framework.Design |
| | | | **Microsoft.Xna.Framework.Content.Pipeline** |
| T-424 | `Microsoft.Xna.Framework.Content.Pipeline/ChildCollection Generic.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-425 | `Microsoft.Xna.Framework.Content.Pipeline/ContentBuildLogger.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-426 | `Microsoft.Xna.Framework.Content.Pipeline/ContentIdentity.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-427 | `Microsoft.Xna.Framework.Content.Pipeline/ContentImporter Generic.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-428 | `Microsoft.Xna.Framework.Content.Pipeline/ContentImporterAttribute.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-429 | `Microsoft.Xna.Framework.Content.Pipeline/ContentImporterContext.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-430 | `Microsoft.Xna.Framework.Content.Pipeline/ContentItem.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-431 | `Microsoft.Xna.Framework.Content.Pipeline/ContentProcessor Generic.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-432 | `Microsoft.Xna.Framework.Content.Pipeline/ContentProcessorAttribute.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-433 | `Microsoft.Xna.Framework.Content.Pipeline/ContentProcessorContext.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-434 | `Microsoft.Xna.Framework.Content.Pipeline/EffectImporter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-435 | `Microsoft.Xna.Framework.Content.Pipeline/ExternalReference Generic.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-436 | `Microsoft.Xna.Framework.Content.Pipeline/FbxImporter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-437 | `Microsoft.Xna.Framework.Content.Pipeline/FontDescriptionImporter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-438 | `Microsoft.Xna.Framework.Content.Pipeline/IContentImporter.xml` | interface | Microsoft.Xna.Framework.Content.Pipeline |
| T-439 | `Microsoft.Xna.Framework.Content.Pipeline/IContentProcessor.xml` | interface | Microsoft.Xna.Framework.Content.Pipeline |
| T-440 | `Microsoft.Xna.Framework.Content.Pipeline/InvalidContentException.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-441 | `Microsoft.Xna.Framework.Content.Pipeline/Mp3Importer.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-442 | `Microsoft.Xna.Framework.Content.Pipeline/NamedValueDictionary Generic.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-443 | `Microsoft.Xna.Framework.Content.Pipeline/OpaqueDataDictionary.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-444 | `Microsoft.Xna.Framework.Content.Pipeline/PipelineComponentScanner.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-445 | `Microsoft.Xna.Framework.Content.Pipeline/PipelineException.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-446 | `Microsoft.Xna.Framework.Content.Pipeline/ProcessorParameter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-447 | `Microsoft.Xna.Framework.Content.Pipeline/ProcessorParameterCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-448 | `Microsoft.Xna.Framework.Content.Pipeline/TargetPlatform.xml` | enum | Microsoft.Xna.Framework.Content.Pipeline |
| T-449 | `Microsoft.Xna.Framework.Content.Pipeline/TextureImporter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-450 | `Microsoft.Xna.Framework.Content.Pipeline/VideoContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-451 | `Microsoft.Xna.Framework.Content.Pipeline/WavImporter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-452 | `Microsoft.Xna.Framework.Content.Pipeline/WmaImporter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-453 | `Microsoft.Xna.Framework.Content.Pipeline/WmvImporter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-454 | `Microsoft.Xna.Framework.Content.Pipeline/XImporter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| T-455 | `Microsoft.Xna.Framework.Content.Pipeline/XmlImporter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline |
| | | | **Microsoft.Xna.Framework.Content.Pipeline.Audio** |
| T-456 | `Microsoft.Xna.Framework.Content.Pipeline.Audio/AudioContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Audio |
| T-457 | `Microsoft.Xna.Framework.Content.Pipeline.Audio/AudioFileType.xml` | enum | Microsoft.Xna.Framework.Content.Pipeline.Audio |
| T-458 | `Microsoft.Xna.Framework.Content.Pipeline.Audio/AudioFormat.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Audio |
| T-459 | `Microsoft.Xna.Framework.Content.Pipeline.Audio/ConversionFormat.xml` | enum | Microsoft.Xna.Framework.Content.Pipeline.Audio |
| T-460 | `Microsoft.Xna.Framework.Content.Pipeline.Audio/ConversionQuality.xml` | enum | Microsoft.Xna.Framework.Content.Pipeline.Audio |
| | | | **Microsoft.Xna.Framework.Content.Pipeline.Graphics** |
| T-461 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/AlphaTestMaterialContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-462 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/AnimationChannel.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-463 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/AnimationChannelDictionary.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-464 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/AnimationContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-465 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/AnimationContentDictionary.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-466 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/AnimationKeyframe.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-467 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/BasicMaterialContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-468 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/BitmapContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-469 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/BoneContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-470 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/BoneWeight.xml` | struct | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-471 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/BoneWeightCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-472 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/DualTextureMaterialContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-473 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/Dxt1BitmapContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-474 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/Dxt3BitmapContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-475 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/Dxt5BitmapContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-476 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/DxtBitmapContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-477 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/EffectContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-478 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/EffectMaterialContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-479 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/EnvironmentMapMaterialContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-480 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/FontDescription.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-481 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/FontDescriptionStyle.xml` | enum | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-482 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/GeometryContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-483 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/GeometryContentCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-484 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/IndexCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-485 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/IndirectPositionCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-486 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/MaterialContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-487 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/MeshBuilder.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-488 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/MeshContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-489 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/MeshHelper.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-490 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/MipmapChain.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-491 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/MipmapChainCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-492 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/NodeContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-493 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/NodeContentCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-494 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/PixelBitmapContent Generic.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-495 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/PositionCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-496 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/SkinnedMaterialContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-497 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/Texture2DContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-498 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/Texture3DContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-499 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/TextureContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-500 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/TextureCubeContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-501 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/TextureReferenceDictionary.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-502 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/VectorConverter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-503 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/VertexChannel.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-504 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/VertexChannel Generic.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-505 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/VertexChannelCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-506 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/VertexChannelNames.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| T-507 | `Microsoft.Xna.Framework.Content.Pipeline.Graphics/VertexContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Graphics |
| | | | **Microsoft.Xna.Framework.Content.Pipeline.Processors** |
| T-508 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/CompiledEffectContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-509 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/EffectProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-510 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/EffectProcessorDebugMode.xml` | enum | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-511 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/FontDescriptionProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-512 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/FontTextureProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-513 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/MaterialProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-514 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/MaterialProcessorDefaultEffect.xml` | enum | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-515 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/ModelBoneContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-516 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/ModelBoneContentCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-517 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/ModelContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-518 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/ModelMeshContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-519 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/ModelMeshContentCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-520 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/ModelMeshPartContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-521 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/ModelMeshPartContentCollection.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-522 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/ModelProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-523 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/ModelTextureProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-524 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/PassThroughProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-525 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/SongContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-526 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/SongProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-527 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/SoundEffectContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-528 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/SoundEffectProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-529 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/SpriteFontContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-530 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/SpriteTextureProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-531 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/TextureProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-532 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/TextureProcessorOutputFormat.xml` | enum | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-533 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/VertexBufferContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-534 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/VertexDeclarationContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| T-535 | `Microsoft.Xna.Framework.Content.Pipeline.Processors/VideoProcessor.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Processors |
| | | | **Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler** |
| T-536 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler/ContentCompiler.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler |
| T-537 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler/ContentTypeWriter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler |
| T-538 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler/ContentTypeWriter Generic.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler |
| T-539 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler/ContentTypeWriterAttribute.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler |
| T-540 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler/ContentWriter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler |
| | | | **Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate** |
| T-541 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate/ContentTypeSerializer.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate |
| T-542 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate/ContentTypeSerializer Generic.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate |
| T-543 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate/ContentTypeSerializer.ChildCallback.xml` | delegate | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate |
| T-544 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate/ContentTypeSerializerAttribute.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate |
| T-545 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate/IntermediateReader.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate |
| T-546 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate/IntermediateSerializer.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate |
| T-547 | `Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate/IntermediateWriter.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate |
| | | | **Microsoft.Xna.Framework.Content.Pipeline.Tasks** |
| T-548 | `Microsoft.Xna.Framework.Content.Pipeline.Tasks/BuildContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Tasks |
| T-549 | `Microsoft.Xna.Framework.Content.Pipeline.Tasks/BuildXact.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Tasks |
| T-550 | `Microsoft.Xna.Framework.Content.Pipeline.Tasks/CleanContent.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Tasks |
| T-551 | `Microsoft.Xna.Framework.Content.Pipeline.Tasks/GetLastOutputs.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Tasks |
| T-552 | `Microsoft.Xna.Framework.Content.Pipeline.Tasks/ICancelBuild.xml` | interface | Microsoft.Xna.Framework.Content.Pipeline.Tasks |
| T-553 | `Microsoft.Xna.Framework.Content.Pipeline.Tasks/ResolveGlobalAssemblies.xml` | class | Microsoft.Xna.Framework.Content.Pipeline.Tasks |

**Total tasks: T-001 through T-553** (551 type XMLs + 1 XSD + 1 index = 553 files)

---

## Execution Order

1. **T-001** — Create `xna.xsd` (schema must exist before any XML can validate)
2. **T-002** — Create `index.xml` (master type index)
3. **T-003 through T-049** — `Microsoft.Xna.Framework` (core runtime, highest C++ audit priority)
4. **T-050 through T-???** — `Microsoft.Xna.Framework.Graphics` (largest namespace)
5. Continue in namespace priority order as listed in the table above

---

## Implementation Notes

- **Deduplication**: HTML files appear twice (v40 and v41). Use v41 only.
- **CDATA**: Wrap all `<summary>`, `<remarks>`, `<syntax>` content in CDATA.
- **Overloads**: Merge all overloads of a method under one `<method>` element.
- **Inherited members**: Do NOT duplicate inherited members; use `baseClass` attribute.
- **Validation**: Every XML must validate against `xna.xsd` before completion.
