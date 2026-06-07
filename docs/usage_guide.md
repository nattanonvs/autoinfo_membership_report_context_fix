# Usage Guide

## ผู้ใช้ทั่วไป (End User)

### Flow หลัก

1. ไปที่ Membership → Reporting → Members Analysis
2. เปิดรายงานในมุมมอง Pivot หรือ Graph
3. ใช้ filter วันที่ (This Month / Custom Range) ได้ตามปกติ

### ผลที่ควรเห็น

- ไม่เกิด RPC_ERROR จากฐานข้อมูลเกี่ยวกับ `invalid input syntax for type date: "1"`

## ผู้ใช้ระดับกลาง (Power User)

- ใช้ Group By เดือน (start_date:month) ได้ตามปกติจาก Pivot/Graph
- ใช้ date filter ที่ `start_date` ได้ตามปกติ

## ผู้ดูแลระบบ (Admin)

### ปิดใช้งานชั่วคราว

1. ไปที่ Settings
2. เลื่อนหา “AutoInfo Membership”
3. ปิด “Enable Membership Report Context Fix”
4. Save

### เปิดกลับ

- ทำซ้ำขั้นตอนเดิม แล้วเปิดสวิตช์กลับเป็น ON และ Save
