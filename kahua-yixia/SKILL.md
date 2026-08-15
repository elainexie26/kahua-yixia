---
name: kahua-yixia
description: Transform one user-supplied JPG, PNG, or WEBP photo into a shareable modern flat illustration or cute animation image while preserving the subject's identity, count, pose, composition, and scene meaning. Use when the user asks to turn a portrait, pet, food, still-life, travel, landscape, or street photo into 现代平面插画风、可爱动画风、插画风、可爱风、萌系、治愈系, or a similar lightweight social-media-ready visual without writing an image prompt.
---

# 咔画一下

把一张现有照片编辑成现代平面插画风或可爱动画风。优先保留“这仍然是用户原来的照片”，再增强风格。

## 接收请求

- 只处理一张 JPG、PNG 或 WEBP 图片；没有图片时请用户上传。
- 需要用户选择 `illustration`（现代平面插画风）或 `cute`（可爱动画风）。未指定时只询问这一项。
- 将 `intensity` 规范为 `weak`、`medium` 或 `strong`；未指定时直接使用 `medium`。
- 保持原图比例、开启主体保留、每次只生成一张图片。
- 不接收自定义艺术家、动画 IP 或品牌官方画风模仿；改写为不指向特定创作者或 IP 的通用视觉特征。

## 执行流程

### 1. 查看照片

- 将用户图片视为**编辑目标**，不是普通风格参考。
- 若图片只有本地文件路径，先用 `view_image` 查看，再使用内置 `image_gen` 编辑。
- 若图片已作为对话附件可见，直接基于该图片编辑。
- 无法读取图片时停止，并请用户重新上传有效文件。

### 2. 建立照片卡

在内部记录以下可见事实，不向用户展示冗长分析：

- 主体：人像、宠物、食物、静物、风景或街景，以及主体数量。
- 识别锚点：人物脸部和发型、宠物品种与花纹、物体类别与轮廓等。
- 构图关系：主体位置、姿态、朝向、遮挡、前后关系和背景结构。
- 画面条件：光线、主色、景深和场景语义。
- 高风险细节：脸、手、眼睛、毛发、文字、规则纹理或密集小物体。

只记录图片中实际可见的内容，不推断身份、地点或其他个人信息。

### 3. 按优先级决策

发生冲突时依次保证：

1. 人物身份、宠物品种或物体类别不变。
2. 主体数量、姿态、位置和核心构图不变。
3. 应用用户选择的风格。
4. 按强度控制转化幅度。
5. 最后处理非必要装饰细节。

### 4. 读取风格预设

每次生成前读取 [references/style-presets.md](references/style-presets.md)，组合所选风格、强度、主体保护规则和照片卡中的可见事实。

### 5. 编译编辑提示词

只把能影响最终像素的信息写入提示词，采用以下紧凑结构：

```text
Use case: style-transfer
Input image: edit target
Primary request: Transform this exact photo into <style preset> at <intensity preset>.
Subject: <visible subject and count>
Scene: <visible setting, lighting, and dominant colors>
Composition: Preserve the original aspect ratio, framing, camera angle, pose, and subject placement.
Identity constraints: <photo-specific recognition anchors>
Constraints: Keep the same subjects, scene meaning, and important background structure.
Avoid: <global avoids plus photo-specific high-risk failures>
```

不要把照片卡标题、产品说明、决策过程、文件路径或未在原图中出现的创意内容写入提示词。

### 6. 生成一次

- 默认使用内置 `image_gen`，不要求 `OPENAI_API_KEY`。
- 本地编辑目标使用 `referenced_image_paths`；只有对话图片而没有本地路径时，使用覆盖该图片所需的最小 `num_last_images_to_include`。两者不得同时使用。
- 明确这是对原照片的编辑，并重复关键不变量。
- 只调用一次并生成一张结果。失败时说明失败并建议重新上传或重试；不要静默改用 CLI，也不要自动连续生成。

### 7. 执行质量门

生成后检查：

- 主体是否仍能辨认，人物脸部、宠物品种或物体类别是否稳定。
- 主体数量、姿态、朝向和关键相对位置是否保持。
- 原图比例、主要构图和背景语义是否基本保持。
- 所选风格和强度是否可见且符合预设。
- 是否新增无关对象，或产生明显的脸、手、眼睛、文字与规则纹理错误。
- 是否出现水印、品牌标识、特定 IP 或艺术家模仿。

若存在明显失败，诚实指出主要问题并询问用户是否重试；不要自行消耗第二次生成。

## 返回结果

- 展示最终图片。
- 用一句话说明所用风格和强度，例如：`已按可爱动画风·中等强度生成，并优先保留原图主体与构图。`
- 预览用途不擅自复制图片。用户指定保存位置或结果供当前项目使用时，再非破坏性地复制到工作区并报告绝对路径。
- 仅在用户明确要求时提供完整提示词或详细分析。

## 隐私与范围

- 只把完成当前编辑所需的图片和提示词交给图片生成服务。
- 不搜索、浏览、分享、提交或上传到其他位置；不永久保存原图。
- 不执行局部修图、去人去物、抠图、批量生成、海报排版、视频或多风格库请求；说明首版范围并建议改用更合适的工具。
