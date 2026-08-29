# 咔画一下

把一张照片转换成现代平面插画或可爱轻卡通图片的 Agent Skill。

- 支持 JPG、PNG、WEBP
- 支持现代平面插画、可爱轻卡通两种风格
- 支持弱、中、强三档强度
- 每次只处理一张图片

## 最简单的安装方法

适用于 ChatGPT 桌面版中的 Codex、Codex CLI 和 Codex IDE 扩展。

1. 打开 Codex。
2. 把下面这句话完整发送给 Codex：

```text
请使用 $skill-installer 安装这个 Skill：https://github.com/elainexie26/kahua-yixia/tree/main/kahua-yixia
```

3. 如果安装后没有看到“咔画一下”，重启 Codex。

安装这个 Skill 不需要填写 API Key，也不需要自己运行代码。生成图片时，Codex 仍需具备可用的图片查看和编辑能力。

## 手动安装（备用方法）

1. 点击 GitHub 页面右上角的 **Code → Download ZIP**。
2. 解压下载的文件。
3. 找到其中的 `kahua-yixia` 文件夹。
4. 把这个文件夹复制到用户目录下的 `.agents/skills` 文件夹中。

Windows：

```text
C:\Users\你的用户名\.agents\skills\kahua-yixia
```

macOS / Linux：

```text
~/.agents/skills/kahua-yixia
```

安装后的结构应当是：

```text
.agents/skills/kahua-yixia/
├── SKILL.md
└── references/
    └── style-presets.md
```

5. 重启 Codex。

## 怎么使用

在 Codex 中上传一张照片，然后发送：

```text
$kahua-yixia 把这张照片转成可爱轻卡通，中等强度。
```

也可以这样说：

```text
$kahua-yixia 把这张照片转成现代平面插画，尽量保持人物数量、姿势和原来的构图。
```

如果没有指定强度，默认使用中等强度。

## 隐私说明

- 仓库不包含 API Key、Token、账号密码或用户照片。
- Skill 只处理用户在当前请求中明确上传并有权使用的一张图片。
- 图片交给编辑服务前，应先向用户说明实际服务方和用途并取得确认。
- Skill 不会自动发布、分享或上传图片到社交平台。
- 涉及他人肖像时，请先取得必要授权。

## 给开发者

普通使用者不需要执行下面的命令。开发者修改 Skill 后，可以运行自检：

```text
python -m pip install PyYAML==6.0.3
python scripts/validate_skill.py
```

发布或提交审核时，只需打包 `kahua-yixia` 目录。

## 许可证

[MIT](./LICENSE)
