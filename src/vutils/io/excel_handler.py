import pandas as pd
from typing import List, Union, Any


class ExcelHandler:
    def __init__(self, excel_file: str, sheet_name: str = "Sheet1"):
        self.df = pd.read_excel(excel_file, sheet_name=sheet_name)

    def getColumns(self) -> List[str]:
        return self.df.columns.values.tolist()

    def getRowSize(self) -> int:
        return len(self.df)

    def setValue(self, row: int, column: str, value: Union[str, int, float]):
        self.df.loc[row, column] = value

    def getValue(self, row: int, column: str) -> Any:
        return self.df.loc[row, column]

    def fillNanFromMergeUnit(self, column: Union[str, List[str]]):
        if isinstance(column, str):
            column = [column]
        for col in column:
            lastValue = None
            for row in self.df.index:
                if pd.isna(self.df.loc[row, col]) and lastValue is not None:
                    self.df.loc[row, col] = lastValue
                elif not pd.isna(self.df.loc[row, col]):
                    lastValue = self.df.loc[row, col]
                else:
                    raise RuntimeError("Unexpected Nan before all!")

    def saveAs(self, filename: str):
        self.df.to_excel(filename, index=False)

    def __str__(self):
        return str(self.df)


if __name__ == '__main__':
    excel = ExcelHandler('./test.xlsx', 'Sheet1')
    print(excel)
    excel.fillNanFromMergeUnit(['问题', '分类'])
    print(excel)
    print(excel.getColumns())
    print(excel[4]['段落'])
