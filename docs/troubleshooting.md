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

## ปัญหา: ปิดใช้งานแล้วแต่ยังเหมือนเดิม

- ตรวจสอบว่าได้ Save ใน Settings แล้ว
- Restart Odoo
- ลองเปิด/ปิดสวิตช์อีกครั้งเพื่อให้ระบบ apply ค่าใหม่

## ปัญหา: มีโมดูลอื่น override action เดียวกัน

- ตรวจสอบค่า action:
  - Settings → Technical → User Interface → Actions → Window Actions
  - เปิด record “Members Analysis” แล้วดู field `Context`
