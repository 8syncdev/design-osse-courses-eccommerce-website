"use client"
import { zodResolver } from "@hookform/resolvers/zod"
import { set, useForm } from "react-hook-form"
import * as z from "zod"

import { Button } from "@/components/ui/button"
import {
    Form,
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/components/ui/form"
import { Input } from "./InputUI"

import { formLoginSchema } from "../schema/lib"
import { FormLoginSchemaType } from "../type"
import { sendEmail } from "@/src/server/actions/sendMail.action"

import { memo, useState } from "react"
import { toast } from "sonner"
import tokenService from "@/src/server/service/token.action"

const styleInput = "text-black bg-white/85 focus:bg-white transition-color duration-300 linear"

const LoginForm = ({
    className = "",
    hidden_content = "Liên Hệ",
    submitting = false,
    setIsSubmiting,
    setOpen,
    children,
}: {
    className?: string,
    hidden_content?: string,
    submitting?: boolean,
    setIsSubmiting?: any,
    setOpen?: any,
    children?: React.ReactNode
}) => {
    // const [isSubmiting, setIsSubmiting] = useState(submitting)
    const form = useForm<FormLoginSchemaType>({
        resolver: zodResolver(formLoginSchema),
        defaultValues: {
            // fullname: "",
            email: "",
            // phone: "",
            // message: "",
            hidden_content: hidden_content,
        },
    })
    const onSubmit = async (data: FormLoginSchemaType) => {
        try {
            let data_res = null
            setIsSubmiting(true)
            data_res = await tokenService.getTokenByEmailOnly(data)
            setIsSubmiting(false)
            form.reset()
            setOpen(false)
            // console.log(data_res)
            if (data_res.code =='res_success') {
                toast("Vui lòng kiểm tra email để xác nhận thông tin")
            }
            else {
                const send_mail_register = await sendEmail(data)
                if (send_mail_register) {
                    toast("Chúng tôi sẽ liên hệ với bạn sớm nhất")
                }
                else {
                    toast("Có lỗi xảy ra, vui lòng thử lại sau")
                }
            }
        }
        catch (err) {
            setIsSubmiting(false)
            toast("Có lỗi xảy ra, vui lòng thử lại sau")
        }
    }

    return (
        <>
            <Form {...form}>
                <form onSubmit={form.handleSubmit(onSubmit)} className={`space-y-2 rounded-md min-w-[17rem] sm:min-w-[25rem] ${className}`}>
                    <FormField
                        control={form.control}
                        name="hidden_content"
                        render={({ field }) => (
                            <FormItem>
                                <FormControl>
                                    <Input type="hidden" className={styleInput} placeholder={``} {...field} />
                                </FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    
                    <FormField
                        control={form.control}
                        name="email"
                        render={({ field }) => (
                            <FormItem className="flex gap-3 items-center">
                                <FormLabel className="text-[1.1rem]">Email</FormLabel>
                                <FormControl>
                                    <Input className={styleInput} placeholder={`Email của bạn`} {...field} />
                                </FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    
                    <FormDescription className="text-center mb-3">
                        Vui lòng kiểm tra email, sau khi gửi để xác nhận thông tin
                    </FormDescription>
                    {children}
                </form>
            </Form>
        </>
    )

}


export default memo(LoginForm)