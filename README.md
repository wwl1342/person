# 个人简历网站

这是一个简约风格的个人简历网站，基于HTML、CSS和JavaScript构建，使用Tailwind CSS进行样式设计。

## 功能特点

- 响应式设计，适配移动端和桌面端
- 平滑滚动效果
- 导航栏滚动时的样式变化
- 清晰的信息结构
- 现代化的UI设计

## 部署到GitHub Pages

### 步骤1：创建GitHub仓库

1. 登录GitHub账号
2. 点击右上角的"+"按钮，选择"New repository"
3. 仓库名称可以设置为 `your-username.github.io`（将your-username替换为你的GitHub用户名）
4. 选择"Public"作为仓库可见性
5. 勾选"Initialize this repository with a README"
6. 点击"Create repository"

### 步骤2：上传文件

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/your-username/your-username.github.io.git
   ```

2. 将本项目中的 `index.html` 文件复制到克隆的仓库目录中

3. 提交并推送更改：
   ```bash
   cd your-username.github.io
   git add index.html
   git commit -m "Add resume website"
   git push origin main
   ```

### 步骤3：启用GitHub Pages

1. 进入仓库的"Settings"页面
2. 滚动到"GitHub Pages"部分
3. 在"Source"下拉菜单中选择"main"分支
4. 点击"Save"
5. 稍等几分钟，你的简历网站就会在 `https://your-username.github.io` 上可用

## 自定义内容

你可以通过编辑 `index.html` 文件来修改个人信息：

- 姓名和职业方向
- 个人基本信息
- 求职意向
- 技能列表
- 工作经历
- 联系方式

## 技术栈

- HTML5
- CSS3 (Tailwind CSS)
- JavaScript
- Font Awesome 图标
