# Troubleshooting

## ปัญหา: เปิด Members Analysis แล้วขึ้น RPC_ERROR

### อาการ

- RPC_ERROR / Odoo Server Error
- PostgreSQL: `psycopg2.errors.InvalidDatetimeFormat: invalid input syntax for type date: "1"`
- Query มักมีรูปแบบ: `WHERE ("report_membership"."start_date" = '1')`

### สาเหตุ

- มีค่าใน action context ที่ทำให้ web client สร้าง domain ผิดรูปแบบ และส่งเข้า `read_group`
- ตัวอย่าง key ที่พบบ่อย:
  - `search_default_start_date: 1`
  - `search_default_member: 1`

### วิธีแก้ (โมดูลนี้)

- เขียนค่า context ให้ปลอดภัย (ไม่ใส่ default ที่ทำให้ domain เทียบ date กับ `1`)
- มีการเก็บค่า context เดิมและ restore ให้ตอน uninstall หรือ disable

### วิธีตรวจเชิงเทคนิค

```bash
python3 /var/odoo/odoo15/odoo/odoo-bin -c <path_to_odoo_conf> shell -d <dbname>
```

```python
action = env.ref("membership.action_report_membership_tree")
print(action.context)
```

## ปัญหา: ปิดใช้งานแล้วแต่ยังเหมือนเดิม

- ตรวจสอบว่าได้ Save ใน Settings แล้ว
- Restart Odoo
- ลองเปิด/ปิดสวิตช์อีกครั้งเพื่อให้ระบบ apply ค่าใหม่

## ปัญหา: Odoo restart แล้วหาโมดูลไม่เจอ

### สาเหตุที่พบบ่อย

- ยังไม่ได้เพิ่ม `/var/odoo/custom15_autoinfo` ใน `addons_path`
- วางโฟลเดอร์โมดูลผิดตำแหน่ง
- owner/permission ของไฟล์ไม่ถูกต้อง

### วิธีแก้

```bash
grep -n "addons_path" <path_to_odoo_conf>
ls -la /var/odoo/custom15_autoinfo
chown -R odoo:odoo /var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix
systemctl restart odoo15
```

## ปัญหา: มีโมดูลอื่น override action เดียวกัน

- ตรวจสอบค่า action:
  - Settings → Technical → User Interface → Actions → Window Actions
  - เปิด record “Members Analysis” แล้วดู field `Context`
- หาก context ถูกเขียนทับหลังติดตั้งโมดูลนี้ ให้ upgrade โมดูลนี้ใหม่อีกครั้ง

## ปัญหา: uninstall แล้วรายงานกลับมา error เดิม

### สาเหตุ

- context เดิมที่ถูก restore กลับมายังมี key ที่ไม่ปลอดภัย
- ระบบเดิมหรือ custom module อื่นเป็นต้นเหตุหลัก

### วิธีรับมือ

1. ติดตั้งหรือ enable โมดูลนี้กลับก่อน
2. ตรวจสอบ source customization ฝั่ง search view/action ของ membership
3. ถ้าต้องถอนถาวร ให้แก้ custom module ต้นเหตุให้เรียบร้อยก่อน
