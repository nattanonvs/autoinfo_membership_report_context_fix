# Update Guide

## Update Version (UI)

1. Apps → ค้นหาโมดูล “AutoInfo Membership Report Context Fix”
2. กด Upgrade

## Update Version (CLI)

```bash
c:\odoo\odoo-15.0\.venv\Scripts\python.exe c:\odoo\odoo-15.0\odoo-bin -c c:\odoo\odoo-15.0\odoo.conf -d <dbname> -u autoinfo_membership_report_context_fix --stop-after-init
```

## Change Log

### 15.0.1.0.1

- ปรับปรุง owner/credits ในเอกสารและ manifest

### 15.0.1.0.0

- เพิ่มกลไกปรับ `context` ของ Members Analysis ให้ไม่สร้าง domain วันที่ผิดรูปแบบ
- เพิ่มการเก็บค่า context เดิม และ restore ให้ตอนถอนการติดตั้ง
- เพิ่มหน้าตั้งค่า (Settings) สำหรับเปิด/ปิดการแก้ไขชั่วคราว
- เพิ่ม test สำหรับยืนยันว่า context ไม่มี `search_default_start_date` และ `search_default_member`

## Timeline

- 2026-06-06
  - วิเคราะห์สาเหตุจาก error `invalid input syntax for type date: "1"`
  - สร้างโมดูล `autoinfo_membership_report_context_fix`
  - ทดสอบติดตั้งและรันทดสอบบน localhost ด้วย config แบบ minimal

- 2026-06-07
  - เพิ่ม Credits และปรับ owner เป็น The Auto-Info Co., Ltd.
