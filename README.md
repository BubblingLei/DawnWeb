# DawnWeb — 外贸宣传站（手工艺品出口）

手工艺品（花篮、陶瓷罐等）出口的宣传网站。目标是上线后被国外客户通过 Google 搜到、且访问速度快。

**参考网站**：superflora.nl（现代自然风外观）+ apac.co.uk（产品分类/列表功能）。

## 技术栈

| 层 | 技术 |
|---|---|
| 前台 | Nuxt 4 + Tailwind CSS + `@nuxtjs/i18n`（中英）+ SEO |
| 后端 | Spring Boot 3 + Java 21 + MySQL（规划中） |
| 后台 | 若依 RuoYi-Vue-Plus（规划中） |

## 目录

```
frontend/   Nuxt 4 前台
backend/    Spring Boot 后端（Phase 2）
admin/      若依后台（Phase 3）
```

## 本地运行

```bash
cd frontend
pnpm install
pnpm dev        # http://localhost:3000
pnpm generate   # 静态生成（部署用）
```

## 部署

- 前台 → Cloudflare Pages
- 域名 → dawnconnections.com
- 站点域名通过环境变量 `NUXT_PUBLIC_SITE_URL` 配置（见 `frontend/.env.example`）
