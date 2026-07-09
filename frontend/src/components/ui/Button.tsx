import type {
  ButtonHTMLAttributes,
  ReactNode,
} from "react"

type Props = ButtonHTMLAttributes<HTMLButtonElement> & {
  children: ReactNode
  active?: boolean
}

export default function Button({
  children,
  active = false,
  className = "",
  ...props
}: Props) {
  return (
    <button
      className={`
        w-full
        rounded-xl
        px-4
        py-3
        text-left
        transition-all
        duration-200

        ${
          active
            ? "bg-blue-600 text-white shadow-lg"
            : "text-slate-300 hover:bg-slate-800 hover:text-white"
        }

        ${className}
      `}
      {...props}
    >
      {children}
    </button>
  )
}