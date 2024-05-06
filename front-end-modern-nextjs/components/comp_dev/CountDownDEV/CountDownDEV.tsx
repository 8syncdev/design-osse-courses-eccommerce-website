'use client'
import { AnimatePresence, motion } from "framer-motion";
import { memo, useEffect, useRef, useState } from "react";

const COUNTDOWN_FROM = "5/30/2024";

const SECOND = 1000;
const MINUTE = SECOND * 60;
const HOUR = MINUTE * 60;
const DAY = HOUR * 24;

const CountDownDEV = ({
    countdownFrom = COUNTDOWN_FROM,
    second=SECOND,
    minute=MINUTE,
    hour=HOUR,
    day=DAY,
    showText = true,
}: {
    countdownFrom?: string;
    second?: number;
    minute?: number;
    hour?: number;
    day?: number;
    showText?: boolean;
}) => {
    const intervalRef = useRef<NodeJS.Timeout | null>(null);

    const [remaining, setRemaining] = useState({
        days: 0,
        hours: 0,
        minutes: 0,
        seconds: 0,
    });

    useEffect(() => {
        intervalRef.current = setInterval(handleCountdown, 1000);

        return () => clearInterval(intervalRef.current || undefined);
    }, []);

    const handleCountdown = () => {
        const end = new Date(COUNTDOWN_FROM);

        const now = new Date();

        const distance = +end - +now;

        const days = Math.floor(distance / DAY);
        const hours = Math.floor((distance % DAY) / HOUR);
        const minutes = Math.floor((distance % HOUR) / MINUTE);
        const seconds = Math.floor((distance % MINUTE) / SECOND);

        setRemaining({
            days,
            hours,
            minutes,
            seconds,
        });
    };

    return (
        <div className="p-5">
            <div className="w-full max-w-5xl mx-auto flex items-center bg-bgsecondary/50 border-2 rounded-md border-[#0ff] shadow-sm-neon h-fit">
                <CountdownItem num={remaining.days} text="ngày" showText={showText} />
                <CountdownItem num={remaining.hours} text="giờ" showText={showText} />
                <CountdownItem num={remaining.minutes} text="phút" showText={showText} />
                <CountdownItem num={remaining.seconds} text="giây" showText={showText} />
            </div>
        </div>
    );
};

const CountdownItem = ({ num, text, showText=true }: {
    num: number;
    text: string;
    showText?: boolean;
}) => {
    return (
        <div className="font-mono w-1/4 h-24 md:h-32 flex flex-col gap-1 md:gap-2 items-center justify-center">
            <div className="w-full text-center relative overflow-hidden">
                <AnimatePresence mode="popLayout">
                    <motion.span
                        key={num}
                        initial={{ y: "100%" }}
                        animate={{ y: "0%" }}
                        exit={{ y: "-100%" }}
                        transition={{ ease: "backIn", duration: 0.75 }}
                        className="block text-2xl md:text-4xl lg:text-6xl xl:text-7xl text-neon font-medium"
                    >
                        {num}
                    </motion.span>
                </AnimatePresence>
            </div>
            {showText && (
                <span className="text-xs md:text-sm lg:text-base text-cyan-100">
                    {text}
                </span>
            )}
        </div>
    );
};

export default memo(CountDownDEV);