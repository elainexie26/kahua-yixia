# 咔画一下

一个面向 Codex 的照片风格化 Skill，可将单张 JPG、PNG 或 WEBP 照片转换为以下两种视觉风格：

- **现代平面插画风**（`illustration`）
- **可爱动画风**（`cute`）

转换过程优先保留主体身份、数量、姿态、构图和场景语义，并支持弱、中、强三档风格强度。

## 安装

将 [`kahua-yixia`](./kahua-yixia) 目录复制到 Codex 的 Skills 目录，然后重新启动或刷新 Codex。

Windows 默认位置：

```text
%USERPROFILE%\.codex\skills\kahua-yixia
```

macOS / Linux 默认位置：

```text
~/.codex/skills/kahua-yixia
```

## 使用

在 Codex 中附上一张照片并调用：

```text
Use $kahua-yixia to turn this photo into a modern flat illustration.
```

也可以直接用中文描述，例如：

```text
请用咔画一下，把这张照片转成可爱动画风，中等强度。
```

## 项目结构

```text
kahua-yixia/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── style-presets.md
```

## 质量与安全

- 遵循 Codex Skill 的标准目录和 YAML 元数据格式。
- 通过 GitHub Actions 自动检查元数据、目录名称、UI 配置和风格预设。
- 不模仿特定在世艺术家、动画 IP、影视作品或品牌官方视觉。
- 不在仓库中保存或上传用户原始照片。
- 默认每次只处理和生成一张图片。

## 许可证

[MIT](./LICENSE)
