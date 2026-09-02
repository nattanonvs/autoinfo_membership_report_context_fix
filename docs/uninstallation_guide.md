# Uninstallation Guide

## Before Uninstall

1. แจ้งผู้ใช้งานที่เกี่ยวข้องว่าระบบอาจกลับไปใช้ context เดิมของรายงานสมาชิก
2. ตรวจสอบว่ามี module อื่นมารับช่วง fix นี้หรือไม่
3. แนะนำให้ backup database ก่อนถอน

## Uninstall (UI)

1. Apps → ค้นหา `AUTO-INFO : Membership Report Context Fix`
2. กด Uninstall

## Uninstall (CLI / Odoo Shell)

หากจำเป็นต้องถอนแบบ command line ให้ใช้ Odoo shell เพื่อเรียก uninstall โดยตรง:

```bash
python3 /var/odoo/odoo15/odoo/odoo-bin shell -c <path_to_odoo_conf> -d <dbname> --no-http
```

```python
module = env["ir.module.module"].search([("name", "=", "autoinfo_membership_report_context_fix")], limit=1)
module.button_immediate_uninstall()
```

หมายเหตุ:

- วิธีนี้ต้องทำโดยผู้ดูแลระบบที่เข้าใจผลกระทบของการ uninstall
- หัวใจสำคัญคือให้ Odoo execute `uninstall_hook` ของโมดูลนี้

## ผลลัพธ์หลังถอนการติดตั้ง

- โมดูลจะ restore ค่า `context` เดิมของ action `membership.action_report_membership_tree` (ถ้ามีการบันทึกไว้ตอนติดตั้ง)
- จากนั้นจะลบค่าที่เก็บไว้ใน `ir.config_parameter` ของโมดูลนี้
- ไฟล์โมดูลใน `/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix` จะยังคงอยู่จนกว่าจะลบออกด้วยตนเอง

## Verify

1. ไปที่ Settings → Technical → Parameters → System Parameters
2. ตรวจสอบว่า key เหล่านี้ไม่เหลืออยู่:
   - `autoinfo_membership_report_context_fix.enabled`
   - `autoinfo_membership_report_context_fix.previous_action_context`
3. เปิดหน้า `Members Analysis` และตรวจสอบพฤติกรรมตาม context เดิมของระบบ

## Remove Source Files

หลังถอนโมดูลแล้ว หากต้องการลบ source ออกจาก server:

```bash
rm -rf /var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix
systemctl restart odoo15
```
