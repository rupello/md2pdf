default:
	just --list


convert path: 
	uv run --script md2pdf.py {{path}} {{path}}.pdf
	
