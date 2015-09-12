global _start

section .data
        align 2
        str:     db 'Hello world!',0xA
        strLen:  equ $-str

section .bss

section .text
        _start:
        mov     rdx, strLen
        mov     rsi, str
        mov     rdi, 1
        mov     rax, 1
        syscall
        mov     rdi, 0
        mov     rax, 231
        syscall
