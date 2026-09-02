# Pause Guide

## Purpose

ใช้เอกสารนี้เมื่อจำเป็นต้องหยุดการทำงานของ fix ชั่วคราวโดยไม่ถอนการติดตั้งโมดูล

## When To Use

- ต้องการตรวจเปรียบเทียบพฤติกรรมก่อนและหลัง apply fix
- ทีมพัฒนาอยากทดสอบ custom module อื่นที่อาจ override action เดียวกัน
- ต้องการวิเคราะห์ incident โดยไม่ถอนโมดูลออกจากระบบ

## Pause By UI

1. ไปที่ `Settings`
2. เลื่อนหา section `AUTO-INFO Membership`
3. ปิด field `Enable Membership Report Context Fix`
4. กด `Save`
5. ทดสอบหน้า `Membership -> Reporting -> Members Analysis`

## Expected Result After Pause

- โมดูลจะ restore ค่า context เดิมที่ถูกเก็บไว้ใน `ir.config_parameter`
- โค้ดโมดูลยังคงติดตั้งอยู่
- สามารถเปิดกลับได้ทันทีโดยไม่ต้อง install ใหม่

## Resume

1. กลับไปที่ `Settings`
2. เปิด field `Enable Membership Report Context Fix`
3. กด `Save`
4. ทดสอบหน้า `Members Analysis` อีกครั้ง

## Operational Notes

- การ pause ไม่ได้ลบ source code ที่ `/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix`
- หาก pause แล้ว error เดิมกลับมา แสดงว่าต้นเหตุเดิมยังมีอยู่และโมดูลนี้เป็นตัวป้องกันอยู่จริง
