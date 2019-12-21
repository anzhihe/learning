# openpyxl模块：处理Excel表格
`pip install openpyxl`
<pre>
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
</pre>

# 从电子表格文件中读取单元格涉及的所有函数、方法和数据类型。
1. 导入 openpyxl 模块。
2. 调用 openpyxl.load_workbook()函数。
3. 取得 Workbook 对象。
4. 调用 get_active_sheet()或 get_sheet_by_name()工作簿方法。
5. 取得 Worksheet 对象。
6. 使用索引或工作表的 cell()方法，带上 row 和 column 关键字参数。
7. 取得 Cell 对象。
8. 读取 Cell 对象的 value 属性。
