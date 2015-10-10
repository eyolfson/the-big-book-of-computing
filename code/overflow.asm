global _start

section .data
	align 2
	str:     db 'Overflow',0xA
	strLen:  equ $-str

section .bss

section .text

_start:
	mov	rdi, 9223372036854775807
	mov	rbx, 1
	add	rdi, rbx
	jo	error
	mov	rax, 231
	syscall
error:
        mov	rdx, strLen
        mov	rsi, str
        mov	rdi, 1
        mov	rax, 1
        syscall
        mov	rdi, 0
        mov	rax, 231
        syscall
