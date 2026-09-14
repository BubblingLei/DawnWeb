# DawnWeb — 外贸宣传站（手工艺品出口）

## 项目简介

为手工艺品出口公司（花篮、陶瓷罐等）制作的外贸宣传网站，目标是**上线后被国外客户通过 Google 搜到、且访问速度快**。

**参考网站**：
- [superflora.nl](https://www.superflora.nl/)（荷兰花卉批发商）→ 现代、自然、美观的视觉外观
- [apac.co.uk](https://www.apac.co.uk/)（B2B 产品目录）→ 产品分类、列表、筛选等功能

## 技术栈

| 层 | 技术 |
|---|---|
| 前台 | Nuxt 3 + Tailwind CSS + `@nuxtjs/i18n`（中英双语）+ SEO |
| 后端 | Spring Boot 3 + Java 21 + MySQL |
| 后台 | 若依 RuoYi-Vue-Plus（阶段3） |
| 部署 | 前台 Cloudflare Pages/Vercel（无需备案、全球快）；后端香港 ECS；域名走 Cloudflare DNS |

## 目录结构

```
DawnWeb/
├── CLAUDE.md      # 本文件
├── frontend/      # Nuxt 3 前台（阶段1）
├── backend/       # Spring Boot 后端（阶段2）
└── admin/         # 若依后台（阶段3）
```

## MVP 页面（4 页 + 中英双语）

1. **首页** — Hero 大图、产品预览、公司简介、询盘 CTA
2. **产品列表** — 分类导航（侧边栏+顶部）、筛选（材质/尺寸）、排序、搜索、产品网格
3. **产品详情** — 大图 + 规格参数表（材质/尺寸/起订量 MOQ）+ "立即询盘"按钮 + 相关推荐
4. **关于我们** — 公司介绍、工厂/工艺、资质
5. **联系我们** — 联系方式 + 询盘表单（姓名/邮箱/国家/产品/留言）

## 常用命令

```bash
# 前台
cd frontend
pnpm install        # 装依赖
pnpm dev            # 开发服务器 http://localhost:3000
pnpm build          # 生产构建
pnpm test           # 单测（Vitest）

# 后端
cd backend
mvn test            # 运行测试
mvn spring-boot:run # 启动

# git
git status
git add -A
git commit -m "<type>: <description>"
```

## 开发约定

- **提交格式**：`<type>: <description>`，type 用 `feat/fix/docs/test/chore/refactor/perf/ci`
- **代码规范**：函数 <50 行、文件 <800 行、嵌套 <4 层、不可变模式（见 `~/.claude/rules/common/coding-style.md`）
- **测试**：新功能走 TDD，覆盖率 80%+（见 `~/.claude/rules/common/testing.md`）
- **安全**：不硬编码密钥、输入校验、防 SQL 注入/XSS（见 `~/.claude/rules/common/security.md`）
- **设计**：拒绝模板脸，现代自然风，遵循 `~/.claude/rules/web/design-quality.md`
- **分支**：GitHub Flow（主干 + feature 分支）

## 开发流程

产品 → 开发 → 测试 → 上线（参考 GitHub Flow + ECC 开发流程）

| 阶段 | 内容 |
|---|---|
| Phase 0 | 初始化（git init、本文件、frontend 脚手架）✅ 进行中 |
| Phase 1 | 前台 4 页 + 分类/筛选/搜索 + i18n + SEO + 询盘表单 |
| Phase 2 | 后端产品/分类/询盘接口 + MySQL |
| Phase 3 | 若依后台管理产品/询盘 |
| Phase 4 | 单测 + E2E |
| Phase 5 | 上线部署 |
