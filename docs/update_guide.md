# Update Guide

## Deployment Path

- โมดูลนี้ต้องถูกวางไว้ที่:

```bash
/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix
```

## Before Upgrade

1. backup database
2. ตรวจสอบว่า source code เวอร์ชันใหม่อยู่ครบ
3. ตรวจสอบว่า service `odoo15` อยู่ในสถานะพร้อมใช้งาน

## Upgrade By CLI

```bash
python3 /var/odoo/odoo15/odoo/odoo-bin -c <path_to_odoo_conf> -d <dbname> -u autoinfo_membership_report_context_fix --no-http --stop-after-init
```

## Upgrade By UI

1. Apps → ค้นหาโมดูล `AUTO-INFO : Membership Report Context Fix`
2. กด Upgrade

## After Upgrade

1. ทดสอบหน้า `Members Analysis`
2. ทดสอบ toggle ที่ Settings
3. ตรวจสอบ log ว่าไม่มี traceback ใหม่จาก module นี้

## Change Log

### 15.0.1.0.3

- เปลี่ยนชื่อแสดงในหน้า Apps เป็น `AUTO-INFO : Membership Report Context Fix`
- เพิ่มโลโก้สำหรับ Apps page และ HTML description
- ขยายเอกสารติดตั้ง/อัปเดต/การใช้งาน/การตั้งค่า/การถอน/การหยุดชั่วคราวให้ละเอียดขึ้น
- เพิ่มคำเตือนสีแดงในคู่มือติดตั้ง

### 15.0.1.0.2

- ปรับปรุง path ในเอกสารให้เป็นมาตรฐาน Linux (/var/odoo/custom15_autoinfo)

### 15.0.1.0.1

- ปรับปรุง owner/credits ในเอกสารและ manifest

### 15.0.1.0.0

- เพิ่มกลไกปรับ `context` ของ Members Analysis ให้ไม่สร้าง domain วันที่ผิดรูปแบบ
- เพิ่มการเก็บค่า context เดิม และ restore ให้ตอนถอนการติดตั้ง
- เพิ่มหน้าตั้งค่า (Settings) สำหรับเปิด/ปิดการแก้ไขชั่วคราว
- เพิ่ม test สำหรับยืนยันว่า context ไม่มี `search_default_start_date` และ `search_default_member`

## Timeline

- 2026-05-19
  - วิเคราะห์สาเหตุจาก error `invalid input syntax for type date: "1"`
  - สร้างโมดูล `autoinfo_membership_report_context_fix`
  - เพิ่ม test และทดสอบติดตั้งบน localhost ด้วย config แบบ minimal
  - เพิ่ม Credits และปรับ owner เป็น The Auto-Info Co., Ltd.
  - ปรับ path ในเอกสารให้เป็นมาตรฐาน Linux
  - เปลี่ยนชื่อหน้า Apps ตามมาตรฐาน AUTO-INFO
  - เพิ่ม logo และ HTML description สำหรับหน้า Apps
  - ขยายเอกสาร deployment, usage, configuration, pause, uninstall และ troubleshooting
