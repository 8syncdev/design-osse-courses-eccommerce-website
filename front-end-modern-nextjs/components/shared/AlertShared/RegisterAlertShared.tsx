'use client'
import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
    AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import React, { useState } from 'react'
import LoginForm from "../FormShared/build/LoginForm"
import { Button } from "@/components/ui/button"
import { X } from "lucide-react"

const RegisterAlertShared = () => {
    const [isSubmiting, setIsSubmiting] = useState(false)
    const [open, setOpen] = useState(false)
    return (
        <AlertDialog open={open}>
            <AlertDialogTrigger className="neon-button" onClick={() => { setOpen(true) }}>Đăng Nhập</AlertDialogTrigger>
            <AlertDialogContent className="bg-bgsecondary border-[#0ff] shadow-sm-neon">
                <AlertDialogHeader>
                    <div className="flex justify-between items-center">
                        <AlertDialogTitle className="text-cyan-50">
                            Đăng Nhập
                        </AlertDialogTitle>
                        <AlertDialogCancel className="bg-bgsecondary border-[#0ff] w-[2.5rem] h-[2.5rem] rounded-full p-0 hover:bg-black" onClick={()=>{setOpen(false)}}>
                            <X className="h-5 w-5"/>
                        </AlertDialogCancel>
                    </div>
                    <AlertDialogDescription className="text-cyan-100">
                        <p>Kiểm tra email để xác nhận tài khoản</p>
                    </AlertDialogDescription>
                </AlertDialogHeader>

                <LoginForm submitting={isSubmiting} setIsSubmiting={setIsSubmiting} setOpen={setOpen}>
                    <div className="w-full flex justify-center">
                        {
                            isSubmiting ?
                                <Button disabled={true}>Đang Gửi...</Button> :
                                <Button type="submit">Xác Nhận</Button>
                        }
                    </div>
                </LoginForm>

            </AlertDialogContent>
        </AlertDialog>

    )
}

export default RegisterAlertShared