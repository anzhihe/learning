from PyPDF2 import PdfFileReader, PdfFileWriter

def watermark(pdfWithoutWatermark, watermarkfile, pdfWithWatermark):

    # 准备合并后的文件对象
    pdfWriter = PdfFileWriter()

    # 打开水印文件
    with open(watermarkfile, 'rb') as f:
        watermarkpage = PdfFileReader(f, strict=False)   

        # 打开需要增加水印的文件
        with open(pdfWithoutWatermark, 'rb') as f:
            pdf_file = PdfFileReader(f, strict=False)

            for i in range(pdf_file.getNumPages()):
                # 从第一页开始处理
                page = pdf_file.getPage(i)
                # 合并水印和当前页
                page.mergePage(watermarkpage.getPage(0))
                # 将合并后的PDF文件写入新的文件
                pdfWriter.addPage(page)

    # 写入新的PDF文件
    with open(pdfWithWatermark, "wb") as f:
        pdfWriter.write(f)

if __name__ == "__main__":
    pdf_without_watermark = "./文章30代码/合同.pdf"
    pdf_with_watermark = "./文章30代码/带水印合同.pdf"
    watermark_file = "./文章30代码/水印.pdf"

    watermark(pdf_without_watermark, watermark_file, pdf_with_watermark)