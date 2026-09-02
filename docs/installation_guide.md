# Installation Guide

<p style="color: red; font-weight: bold;">
Critical Warning: ติดตั้งโมดูลนี้เฉพาะในเครื่อง/ฐานข้อมูลที่มีโมดูล <code>membership</code> ใช้งานอยู่จริงเท่านั้น และต้องวางโมดูลไว้ใต้ <code>/var/odoo/custom15_autoinfo</code> ให้ถูกต้องก่อน restart service หากใส่ path ผิด, ใช้ database ผิด, หรือ restart โดยที่ addons_path ยังไม่รวม path นี้ อาจทำให้ Odoo โหลด registry ไม่ครบ, module list เพี้ยน, หรือ service start ไม่ขึ้นได้
</p>

<p style="color: red;">
ก่อนติดตั้งใน production แนะนำให้ backup database และ backup ไฟล์ config ทุกครั้ง และหากจะรันคำสั่ง <code>odoo-bin</code> แบบ standalone ให้ใช้ <code>--no-http</code> หรือหยุด service หลักก่อนเสมอ เพื่อหลีกเลี่ยง port conflict
</p>

## Prerequisites

- Odoo 15
- ตำแหน่งติดตั้งโมดูลต้องเป็น `/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix`
- `addons_path` ในไฟล์ config ต้องมี `/var/odoo/custom15_autoinfo`
- Database เป้าหมายต้องติดตั้งโมดูล `membership` แล้ว
- ผู้ดูแลระบบต้องมีสิทธิ์ restart service และ upgrade module

## Recommended Pre-Checks

1. ตรวจสอบ path:

```bash
ls -la /var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix
```

2. ตรวจสอบว่า `addons_path` มี path นี้จริง:

```bash
grep -n "addons_path" <path_to_odoo_conf>
```

3. ตรวจสอบสถานะ service:

```bash
systemctl status odoo15 --no-pager
```

4. สำรองฐานข้อมูลก่อน:

```bash
pg_dump -Fc -d <dbname> -f <backup_path>/<dbname>_before_autoinfo_membership_report_context_fix.dump
```

## Install By Copying Module

1. คัดลอกโฟลเดอร์โมดูลไปไว้ที่:

```bash
/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix
```

2. ตั้ง owner/permission ให้สอดคล้องกับ service account ของ Odoo:

```bash
chown -R odoo:odoo /var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix
find /var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix -type d -exec chmod 755 {} \;
find /var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix -type f -exec chmod 644 {} \;
```

## Install (CLI - Recommended)

1. Restart service เพื่อให้ Odoo มองเห็นโมดูล:

```bash
systemctl restart odoo15
```

2. Upgrade module list และติดตั้งโมดูล:

```bash
python3 /var/odoo/odoo15/odoo/odoo-bin -c <path_to_odoo_conf> -d <dbname> -i autoinfo_membership_report_context_fix --no-http --stop-after-init
```

3. ถ้าใช้งานผ่าน service ตามปกติ ให้ start กลับ:

```bash
systemctl start odoo15
```

## Install (UI)

1. เปิด Odoo ด้วย config ที่ใช้งานจริง
2. ไปที่ Apps → Update Apps List
3. ค้นหา `AUTO-INFO : Membership Report Context Fix`
4. กด Install

## Post-Install Verification

1. ไปที่ `Membership -> Reporting -> Members Analysis`
2. เปิดมุมมอง Pivot และ Graph
3. ทดสอบการกรองวันที่
4. ไปที่ `Settings` และตรวจสอบว่ามี section `AUTO-INFO Membership`
5. ตรวจสอบว่า toggle `Enable Membership Report Context Fix` เป็น ON

## Technical Verification

```bash
python3 /var/odoo/odoo15/odoo/odoo-bin -c <path_to_odoo_conf> shell -d <dbname> --no-http
```

จากนั้นตรวจค่า action:

```python
action = env.ref("membership.action_report_membership_tree")
print(action.context)
```

ค่าที่คาดหวัง:

- ไม่มี `search_default_start_date`
- ไม่มี `search_default_member`

## Rollback If Needed

ถ้าพบปัญหาหลังติดตั้ง:

1. ปิดการใช้งานชั่วคราวจาก Settings
2. หากยังมีปัญหาให้ถอนโมดูล
3. หากต้องการ rollback เต็มรูปแบบให้ restore database backup ที่ทำไว้ก่อนติดตั้ง
