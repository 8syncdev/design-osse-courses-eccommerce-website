import * as z from "zod"

export const formLoginSchema = z.object({
    email: z.string({
        required_error: "Email không được để trống",
        invalid_type_error: "Email phải là chuỗi",
        description: "Email của bạn",
    }).email({
        message: "Email không hợp lệ",
    }).max(50, {
        message: "Email không được quá 50 ký tự",
    }).min(10, {
        message: "Email không được ít hơn 10 ký tự",
    }),
    hidden_content: z.string().max(100).optional(),
})
