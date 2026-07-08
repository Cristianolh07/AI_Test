import pandas as pd
import os

def create_and_process_invoice():
    # 1. 生成模拟数据
    data = {
        '单号': ['INV001', 'INV002', 'INV003', 'INV004', 'INV005'],
        '金额': [450, 600, 300, 800, 150],
        '备注': ['', '', '普通发票', '', '小额测试']
    }
    df = pd.DataFrame(data)
    
    # 2. 保存为 test_invoice.xlsx
    test_file = 'test_invoice.xlsx'
    df.to_excel(test_file, index=False)
    print(f"已生成原始文件: {test_file}")
    
    # 3. 读取文件并处理
    # 读取刚才生成的文件
    df_read = pd.read_excel(test_file)
    
    # 如果‘金额’大于 500，在‘备注’里加上‘需要人工复核’
    # 使用 .loc 进行安全更新
    mask = df_read['金额'] > 500
    
    # 处理备注：如果是空的则直接赋值，如果不为空则追加内容
    def update_remark(row):
        if row['金额'] > 500:
            original_remark = str(row['备注']) if pd.notna(row['备注']) and row['备注'] != '' else ''
            if original_remark:
                return f"{original_remark}; 需要人工复核"
            else:
                return "需要人工复核"
        return row['备注']

    df_read['备注'] = df_read.apply(update_remark, axis=1)
    
    # 4. 保存为 processed_invoice.xlsx
    processed_file = 'processed_invoice.xlsx'
    df_read.to_excel(processed_file, index=False)
    print(f"已生成处理后的文件: {processed_file}")

if __name__ == "__main__":
    create_and_process_invoice()
