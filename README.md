# 咔画一下

“咔画一下”是一个平台中立的照片风格化 Skill：将用户有权使用的一张 JPG、PNG 或 WEBP 照片转换为现代平面插画或可爱轻卡通静态图。

## 发布内容

提交审核时仅打包 `kahua-yixia` 目录。发布包包含：

```text
kahua-yixia/
├── SKILL.md
└── references/
    └── style-presets.md
```

Skill 不包含可执行代码、密钥、账号操作或自动发布功能。它只在宿主已经提供图片查看与编辑能力、能够披露实际服务方及数据规则，并取得用户确认后执行。

## 自检

运行：

```text
python scripts/validate_skill.py
```

自检会检查元数据、文件结构、风格名称、引用文件，以及发布内容中是否残留平台专属工具名称。

## 许可证

[MIT](./LICENSE)
