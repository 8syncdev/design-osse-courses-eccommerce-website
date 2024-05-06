import { formLoginSchema } from "./schema/lib";
import * as z from "zod"

export type FormLoginSchemaType = z.infer<typeof formLoginSchema>