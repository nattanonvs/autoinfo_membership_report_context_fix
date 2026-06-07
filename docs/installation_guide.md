# Installation Guide

## Prerequisites

- Odoo 15
- Addons path ต้องมี `C:\odoo\APPreadytouse` (ในเครื่องนี้มีอยู่แล้วในไฟล์ config)

## Install (UI)

1. เปิด Odoo ด้วย config ที่ใช้งานจริง
2. ไปที่ Apps → Update Apps List
3. ค้นหา “AutoInfo Membership Report Context Fix”
4. กด Install

## Install (CLI)

ตัวอย่าง (ปรับชื่อ database ตามจริง):

```bash
c:\odoo\odoo-15.0\.venv\Scripts\python.exe c:\odoo\odoo-15.0\odoo-bin -c c:\odoo\odoo-15.0\odoo.conf -d <dbname> -i autoinfo_membership_report_context_fix --stop-after-init
```

## Verify

- ไปที่ Membership → Reporting → Members Analysis
- ระบบต้องไม่ขึ้น RPC_ERROR และสามารถเปิด pivot/graph ได้ตามปกติ
