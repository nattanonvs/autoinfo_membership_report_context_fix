# AutoInfo Membership Report Context Fix (Odoo 15)

โมดูลนี้แก้ปัญหา RPC_ERROR ของรายงาน Members Analysis (membership) ที่เกิดจากการมีค่า default context บางตัวทำให้ระบบสร้าง domain วันที่ผิดรูปแบบ (เช่นเทียบ date กับค่า `1`) และทำให้ PostgreSQL error `invalid input syntax for type date: "1"`.

## Scope (Case 1: แก้ไขอยู่ในโมดูลเดียว)

- โมดูลเดิมที่เกี่ยวข้อง: `membership`
- จุดที่แก้: `ir.actions.act_window` (xml id: `membership.action_report_membership_tree`)
- วิธีแก้: ปรับค่า `context` ให้เป็นค่าที่ปลอดภัย และเก็บค่าเดิมไว้เพื่อ restore ตอนถอนการติดตั้ง

## คุณค่า (Value)

- ลด downtime ของหน้ารายงาน Members Analysis
- ทำให้ผู้ใช้เข้าเมนูรายงานได้ทันทีโดยไม่เจอ error ฝั่งฐานข้อมูล
- ติดตั้ง/ถอนการติดตั้งได้โดยไม่แก้ core และมีการ restore ค่าเดิมให้

## วิธีใช้งานแบบย่อ

- ติดตั้งโมดูล แล้วใช้งานเมนู: Membership → Reporting → Members Analysis ตามปกติ
- ปิดใช้งานชั่วคราวได้ที่ Settings → AutoInfo Membership → “Enable Membership Report Context Fix”

## เอกสาร

- [installation_guide.md](/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix/docs/installation_guide.md)
- [uninstallation_guide.md](/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix/docs/uninstallation_guide.md)
- [update_guide.md](/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix/docs/update_guide.md)
- [usage_guide.md](/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix/docs/usage_guide.md)
- [configuration_guide.md](/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix/docs/configuration_guide.md)
- [troubleshooting.md](/var/odoo/custom15_autoinfo/autoinfo_membership_report_context_fix/docs/troubleshooting.md)

## Owner

- The Auto-Info Co., Ltd.

## Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).
