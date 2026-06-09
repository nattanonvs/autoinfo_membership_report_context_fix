# Installation Guide

## Prerequisites

- Odoo 15
- Addons path ต้องมี `/var/odoo/custom15_autoinfo`

## Install (UI)

1. เปิด Odoo ด้วย config ที่ใช้งานจริง
2. ไปที่ Apps → Update Apps List
3. ค้นหา “AutoInfo Membership Report Context Fix”
4. กด Install

## Install (CLI)

ตัวอย่าง (ปรับชื่อ database ตามจริง):

```bash
python3 /var/odoo/odoo15/odoo/odoo-bin -c <path_to_odoo_conf> -d <dbname> -i autoinfo_membership_report_context_fix --stop-after-init
```

## Verify

- ไปที่ Membership → Reporting → Members Analysis
- ระบบต้องไม่ขึ้น RPC_ERROR และสามารถเปิด pivot/graph ได้ตามปกติ
