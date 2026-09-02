# Usage Guide

## ภาพรวมการใช้งาน

โมดูลนี้ไม่มีเมนูธุรกิจใหม่ แต่จะเปลี่ยนพฤติกรรมของ action เดิมในรายงาน Members Analysis ให้ปลอดภัยขึ้น ผู้ใช้จึงยังใช้งาน flow เดิมของระบบ แต่ไม่ควรเจอ RPC error เดิมอีก

## ผู้ใช้ทั่วไป (End User)

### Flow หลัก

1. ไปที่ Membership → Reporting → Members Analysis
2. เปิดรายงานในมุมมอง Pivot หรือ Graph
3. ใช้ filter วันที่ (This Month / Custom Range) ได้ตามปกติ
4. ตรวจสอบว่ารายงานแสดงผลโดยไม่เด้ง error popup

### ผลที่ควรเห็น

- ไม่เกิด RPC_ERROR จากฐานข้อมูลเกี่ยวกับ `invalid input syntax for type date: "1"`
- สามารถสลับมุมมอง Pivot, Graph และ List ได้ต่อเนื่อง

### ตัวอย่างการใช้งาน

- ตัวอย่างที่ 1: ดูรายงานสมาชิกของเดือนปัจจุบัน
  - เข้า Members Analysis
  - ใช้ filter เดือนปัจจุบัน
  - ระบบต้องแสดงผลโดยไม่ล้ม
- ตัวอย่างที่ 2: วิเคราะห์แนวโน้มแบบรายเดือน
  - เปิด Graph view
  - ใช้ Group By เดือน
  - ระบบต้องประมวลผลได้ปกติ

## ผู้ใช้ระดับกลาง (Power User)

- ใช้ Group By เดือน (start_date:month) ได้ตามปกติจาก Pivot/Graph
- ใช้ date filter ที่ `start_date` ได้ตามปกติ
- ใช้ export/report analysis ต่อได้ตาม flow เดิมของ `membership`

### ข้อควรตรวจสอบ

- หากมี favorite filter เดิมที่สร้างก่อนติดตั้งโมดูล ให้ลองเปิดใช้งานและตรวจสอบว่ารายงานยังแสดงผลปกติ
- หากมี custom search view เพิ่มเติม ควรทดสอบร่วมกับ filter วันที่ทุกตัว

## ผู้ดูแลระบบ (Admin)

### ปิดใช้งานชั่วคราว

1. ไปที่ Settings
2. เลื่อนหา “AUTO-INFO Membership”
3. ปิด “Enable Membership Report Context Fix”
4. Save
5. ทดสอบเปิดหน้า Members Analysis อีกครั้งเพื่อยืนยันผล

### เปิดกลับ

- ทำซ้ำขั้นตอนเดิม แล้วเปิดสวิตช์กลับเป็น ON และ Save

### Flow สำหรับผู้ดูแลระบบ

1. ติดตั้งโมดูล
2. ตรวจสอบ `Members Analysis`
3. ตรวจสอบ Settings ว่า toggle ทำงาน
4. บันทึกผลการทดสอบใน change management ภายในองค์กร

### หมายเหตุ

- โมดูลนี้แก้เฉพาะ action context ของรายงานสมาชิก
- หากมีโมดูลอื่นเข้ามาเขียนทับ action เดียวกันภายหลัง อาจต้อง re-apply โดย upgrade โมดูลนี้อีกครั้ง
