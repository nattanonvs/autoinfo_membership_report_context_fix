# Configuration Guide

## Settings UI

- เมนู: Settings → AUTO-INFO Membership
- ฟิลด์หลัก: `Enable Membership Report Context Fix`
- ความหมายของค่า:
  - เปิด: ระบบจะเขียน context แบบปลอดภัยให้กับ `membership.action_report_membership_tree`
  - ปิด: ระบบจะ restore context เดิมที่เคยเก็บไว้ตอนติดตั้งโมดูล

## Recommended Deployment Path

- ตัวโมดูลควรถูกวางไว้ที่:

```bash
/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix
```

## System Parameters

โมดูลใช้ `ir.config_parameter` สำหรับเก็บค่า:

- `autoinfo_membership_report_context_fix.enabled`
  - ค่า: `True` / `False`
  - ค่าเริ่มต้น: `True`
  - หน้าที่: ควบคุมว่าโมดูลจะ apply safe context หรือ restore context เดิม
- `autoinfo_membership_report_context_fix.previous_action_context`
  - ค่า: string ของ `context` เดิมของ action
  - หน้าที่: เก็บ backup context เดิมของ action เพื่อใช้ตอน disable/uninstall

## Action Affected

- XML ID: `membership.action_report_membership_tree`
- Model: `ir.actions.act_window`
- Field ที่เปลี่ยน: `context`

## Safe Context Applied By This Module

```python
{
    "group_by_no_leaf": 1,
    "search_default_Revenue": 1,
    "search_default_salesman": 1,
    "search_default_this_month": 1,
}
```

## Configuration Best Practices

- เปิดใช้งาน fix นี้ไว้ตลอดใน production
- ก่อน disable ให้แจ้งทีมที่ใช้งานรายงานสมาชิก เพราะ error เดิมอาจกลับมาได้
- หลังติดตั้งโมดูลอื่นที่แตะรายงาน membership ให้ recheck ค่า `action.context`
- ในกรณีทำ deployment ผ่าน CI/CD ให้เพิ่ม post-deploy step เพื่อตรวจว่า module ยังติดตั้งและเปิดใช้งานอยู่

## Validation Checklist

- หน้า `Members Analysis` เปิดได้ปกติ
- ไม่มี `search_default_start_date` ใน context สุดท้าย
- ไม่มี `search_default_member` ใน context สุดท้าย
- Toggle ใน Settings ทำงานได้ทั้งเปิดและปิด
