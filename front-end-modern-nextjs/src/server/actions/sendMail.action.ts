"use server"
import { FormLoginSchemaType } from '@/components/shared/FormShared/type'
import nodemailer from 'nodemailer';
import Mail from 'nodemailer/lib/mailer';
/**
 * todo npm i nodemailer
 * todo npm i @types/nodemailer
 */

const connectAndSendEmail = async (email: string, content: string) => {
    const transport = nodemailer.createTransport({
        service: 'gmail',
        /* 
          setting service as 'gmail' is same as providing these setings:
          host: "smtp.gmail.com",
          port: 465,
          secure: true
          If you want to use a different email provider other than gmail, you need to provide these manually.
          Or you can go use these well known services and their settings at
          https://github.com/nodemailer/nodemailer/blob/master/lib/well-known/services.json
      */
        auth: {
            user: process.env.MY_EMAIL,
            pass: process.env.MY_PASSWORD,
        },
    });

    const mailOptions: Mail.Options = {
        from: process.env.MY_EMAIL,
        to: [process.env.MY_EMAIL as string, email],
        // cc: email, (uncomment this line if you want to send a copy to the sender)
        subject: `Liên hệ từ ${process.env.MY_EMAIL}`,
        text: `\nNội dung: ${content},\nEmail: ${email}, Cảm ơn bạn đã liên hệ với chúng tôi. Chúng tôi sẽ phản hồi sớm nhất có thể trong 48 giờ 🥰\nZalo Admin: https://zalo.me/0703930513`,
    };

    const sendMailPromise = () =>
        new Promise<string>((resolve, reject) => {
            transport.sendMail(mailOptions, function (err) {
                if (!err) {
                    resolve('Email sent');
                } else {
                    reject(err.message);
                }
            });
        });

    try {
        await sendMailPromise();
    } catch (err) {
        // console.log(err);
        return 'send_email_fail';
    }
}



export const sendEmail = async (data: FormLoginSchemaType) => {
    // console.log(data);

    const email = data.email;
    const content = data.hidden_content as string;
    try {
        await connectAndSendEmail(email, content);
        return true;
    }
    catch (err) {
        // console.log(err);
        return false;
    }
}