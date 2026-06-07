# Uninstallation Guide

## Uninstall (UI)

1. Apps → ค้นหา “AutoInfo Membership Report Context Fix”
2. กด Uninstall

## ผลลัพธ์หลังถอนการติดตั้ง

- โมดูลจะ restore ค่า `context` เดิมของ action `membership.action_report_membership_tree` (ถ้ามีการบันทึกไว้ตอนติดตั้ง)
- จากนั้นจะลบค่าที่เก็บไว้ใน `ir.config_parameter` ของโมดูลนี้

## Verify

- ไปที่ Settings → Technical → Parameters → System Parameters
  - ตรวจสอบว่า key เหล่านี้ไม่เหลืออยู่:
    - `autoinfo_membership_report_context_fix.enabled`
    - `autoinfo_membership_report_context_fix.previous_action_context`
