# Configuration Guide

## Settings UI

- เมนู: Settings → AutoInfo Membership
- ฟิลด์:
  - “Enable Membership Report Context Fix”
    - เปิด: ระบบจะเขียน context แบบปลอดภัยให้กับ `membership.action_report_membership_tree`
    - ปิด: ระบบจะ restore context เดิมที่เคยเก็บไว้ตอนติดตั้งโมดูล

## System Parameters

โมดูลใช้ `ir.config_parameter` สำหรับเก็บค่า:

- `autoinfo_membership_report_context_fix.enabled`
  - ค่า: `True` / `False`
  - ค่าเริ่มต้น: `True`
- `autoinfo_membership_report_context_fix.previous_action_context`
  - ค่า: string ของ `context` เดิมของ action

## Best Practices

- แนะนำให้ “Enable” ไว้ตลอดสำหรับ production
- หากมีโมดูลอื่น override action เดียวกัน ให้ตรวจสอบว่า context สุดท้ายไม่มี `search_default_start_date` และ `search_default_member`
