# AUTO-INFO : Membership Report Context Fix

โมดูลนี้ออกแบบมาเพื่อแก้ปัญหา `RPC_ERROR` ในรายงาน Members Analysis ของ Odoo 15 ซึ่งเกิดจาก action context เดิมส่งค่า default ที่ทำให้ระบบสร้าง domain วันที่ผิดรูปแบบ เช่น `('start_date', '=', 1)` และนำไปสู่ PostgreSQL error `invalid input syntax for type date: "1"`.

## Module Path

- Production path ที่แนะนำ: `/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix`

## Business Value

- ลดความเสี่ยงที่ผู้ใช้งานเข้าเมนูรายงานสมาชิกแล้วระบบล้ม
- ลดเวลาวิเคราะห์ incident เพราะสาเหตุถูกควบคุมไว้ที่ action context โดยตรง
- ติดตั้งและถอนการติดตั้งได้โดยไม่ต้องแก้ไข core module ของ Odoo
- รองรับการปิดใช้งานชั่วคราวจากหน้า Settings โดยยังเก็บค่าเดิมไว้ restore ได้

## Functional Scope

- โมดูลอ้างอิงต้นทาง: `membership`
- จุดที่แก้ไข: `membership.action_report_membership_tree`
- วิธีทำงาน:
  - เก็บค่า `context` เดิมของ action ก่อน
  - เขียน `context` แบบปลอดภัยเมื่อเปิดใช้งานโมดูล
  - คืนค่า `context` เดิมเมื่อ disable หรือ uninstall

## Main Documents

- [docs/installation_guide.md](docs/installation_guide.md)
- [docs/uninstallation_guide.md](docs/uninstallation_guide.md)
- [docs/update_guide.md](docs/update_guide.md)
- [docs/usage_guide.md](docs/usage_guide.md)
- [docs/configuration_guide.md](docs/configuration_guide.md)
- [docs/troubleshooting.md](docs/troubleshooting.md)
- [docs/pause_guide.md](docs/pause_guide.md)

## Owner

- The Auto-Info Co., Ltd.

## Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon - Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).
