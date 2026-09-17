"""生成客户产品数据填写表 docs/product-data-template.xlsx。

用法:
    python docs/generate_template.py

产物为一个 3-sheet 的问卷式 Excel:
    Instructions  填写说明 + 图片命名规范
    Products      主表（14 列，含级联下拉、季节只填 Yes、示例行）
    Categories    6 大类 / 18 子类对照 + 图片前缀（同时是二级下拉的数据源）

数据模型（已与客户商定的极简版）:
    款号 / 产品名称 / Top / Height / Base / 一级分类 / 二级分类 / 7 个季节节日(只填 Yes)
    图片不填列，按 `{前缀}{款号}.jpg` 命名后打包发送。

列顺序：尺寸（Top/Height/Base）在分类之前。
分类采用「级联下拉」：先选一级分类（6 项），二级分类自动过滤为该类下的 2~5 项。
季节/节日：只在对的季节列选 Yes，其余留空即可（不用填 No）。
"""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation

# --------------------------------------------------------------------------- #
# 常量（与后端 seed 数据保持一致）
# --------------------------------------------------------------------------- #

# (一级分类, 图片前缀, [子分类...])
CATEGORIES: list[tuple[str, str, list[str]]] = [
    ("Basket", "B", [
        "Willow basket",
        "Wooden basket",
        "Paper-Cotton Rope Basket",
        "Grass basket",
        "Fabric pot",
    ]),
    ("Tin Pot", "T", [
        "Zinc tin pot",
        "Printed tin pot",
    ]),
    ("Glass", "G", [
        "Man blown glass",
        "Machine made glass",
    ]),
    ("Ceramic", "C", [
        "Dolomite pots",
        "Cement pot",
    ]),
    ("Decorations", "D", [
        "Hanging Deco",
        "Picks Deco",
        "LED light",
        "Felt deco",
        "Wreath-Garland",
    ]),
    ("Greenhouse", "Gr", [
        "Steel Connectors",
        "Alu. Connectors",
    ]),
]

# 无需填写尺寸的二级分类（Top/Height/Base 留空）
NO_SIZE_TOP_LEVEL = {"Decorations", "Greenhouse"}

# 季节/节日（多选：只在对的列填 Yes，其余留空）
SEASONS: list[str] = [
    "Valentine's Day",
    "Spring/Summer",
    "Autumn",
    "Halloween",
    "Christmas",
    "Mother's Day",
    "Easter",
]

# 一级分类下拉（内联，6 项，字符数远小于 255 上限）
TOP_LEVELS = [top for top, _, _ in CATEGORIES]

# 主表列（14 列）：尺寸在分类之前
HEADERS: list[str] = [
    "款号", "产品名称", "Top(cm)", "Height(cm)", "Base(cm)",
    "一级分类", "二级分类",
    *SEASONS,
]

# 按表头名推导列号（1-based），避免硬编码
def col_idx(header: str) -> int:
    return HEADERS.index(header) + 1


SIZE_START = col_idx("Top(cm)")
SIZE_END = col_idx("Base(cm)")
TOP_COL = col_idx("一级分类")
SUB_COL = col_idx("二级分类")
SEASON_START = col_idx(SEASONS[0])
SEASON_END = col_idx(SEASONS[-1])

SIZE_COLS = set(range(SIZE_START, SIZE_END + 1))
SEASON_COLS = set(range(SEASON_START, SEASON_END + 1))
IDENTITY_COLS = {1, 2, TOP_COL, SUB_COL}

SAMPLE_ROW_SIZED = {
    "款号": "1001",
    "产品名称": "Woven Willow Basket",
    "Top(cm)": 30,
    "Height(cm)": 28,
    "Base(cm)": 22,
    "一级分类": "Basket",
    "二级分类": "Willow basket",
    "Spring/Summer": "Yes",
    "Christmas": "Yes",
}
SAMPLE_ROW_NO_SIZE = {
    "款号": "2001",
    "产品名称": "Frosted Hanging Ornament",
    "一级分类": "Decorations",
    "二级分类": "Hanging Deco",
    "Christmas": "Yes",
}

OUTPUT = Path(__file__).parent / "product-data-template.xlsx"

# --------------------------------------------------------------------------- #
# 样式
# --------------------------------------------------------------------------- #

FILL_IDENTITY = PatternFill("solid", fgColor="2F5B3B")  # 深绿：基础信息
FILL_SIZE = PatternFill("solid", fgColor="1D4ED8")      # 蓝：尺寸
FILL_SEASON = PatternFill("solid", fgColor="B45309")    # 赭石：季节/节日
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
EXAMPLE_FILL = PatternFill("solid", fgColor="EAF3EC")
NOTE_FONT = Font(italic=True, color="6B7280", size=10)
THIN = Side(style="thin", color="D1D5DB")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(vertical="top", wrap_text=True)
CENTER = Alignment(horizontal="center", vertical="center")


def header_fill_for(col_idx: int) -> PatternFill:
    if col_idx in SEASON_COLS:
        return FILL_SEASON
    if col_idx in SIZE_COLS:
        return FILL_SIZE
    return FILL_IDENTITY


def style_header_row(ws, headers: list[str]) -> None:
    for idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=idx, value=header)
        cell.fill = header_fill_for(idx)
        cell.font = HEADER_FONT
        cell.alignment = CENTER
        cell.border = BORDER


def set_col_widths(ws, widths: dict[int, float]) -> None:
    for col, width in widths.items():
        ws.column_dimensions[get_column_letter(col)].width = width


# --------------------------------------------------------------------------- #
# Sheet 1: Instructions
# --------------------------------------------------------------------------- #

def build_instructions(ws) -> None:
    ws.title = "Instructions"
    ws.sheet_view.showGridLines = False
    set_col_widths(ws, {1: 120})

    lines: list[tuple[str, str | None]] = [
        ("title", "产品数据填写说明（Product Data — Instructions）"),
        ("space", None),
        ("h", "1. 只需填写 Products 表"),
        ("p", "每个产品占一行。带下拉的列直接点选，不要手输文字。"),
        ("space", None),
        ("h", "2. 列说明（按表格从左到右的顺序）"),
        ("p", "· 款号（Style No.）：客户自己的产品编号，必须唯一，例如 1001、A-2002。"),
        ("p", "· 产品名称（Name）：英文名称，例如 Woven Willow Basket。"),
        ("p", "· Top / Height / Base：顶部口径 / 高度 / 底部直径，单位 cm，填数字即可。"),
        ("p", "· 一级分类 → 二级分类：先选大类（6 个），再选小类（会自动筛选出该类下的 2~5 项）。"),
        ("p", "· 季节/节日（Seasons & Festivals）：只在对的季节列选 Yes，其余留空即可，不用填 No。"),
        ("space", None),
        ("h", "3. 哪些产品不用填尺寸"),
        ("p", "Decorations（挂饰/花艺饰品）与 Greenhouse（温室连接件）两类，Top / Height / Base 三列留空。"),
        ("space", None),
        ("h", "4. 图片命名规则（不用在表里填图片列）"),
        ("p", "每个产品一张图，文件名 = 图片前缀 + 款号 + .jpg。"),
        ("p", "图片前缀查 Categories 表：Basket=B、Tin Pot=T、Glass=G、Ceramic=C、Decorations=D、Greenhouse=Gr。"),
        ("p", "例如：款号 1001 的 Willow basket → B1001.jpg；款号 2001 的 Hanging Deco → D2001.jpg。"),
        ("p", "填完表后，把按此规则命名的图片打包发回即可。"),
        ("space", None),
        ("h", "5. 提示"),
        ("p", "示例行（第 2、3 行）只是演示，填写前请删掉或用真实数据覆盖。"),
    ]

    row = 1
    for kind, text in lines:
        if kind == "space":
            row += 1
            continue
        cell = ws.cell(row=row, column=1, value=text)
        if kind == "title":
            cell.font = Font(bold=True, size=15, color="2F5B3B")
        elif kind == "h":
            cell.font = Font(bold=True, size=12, color="1F2937")
        else:
            cell.font = Font(size=11, color="374151")
            cell.alignment = WRAP
        row += 1


# --------------------------------------------------------------------------- #
# Sheet 2: Products（主表）
# --------------------------------------------------------------------------- #

def build_products(ws) -> None:
    ws.title = "Products"

    style_header_row(ws, HEADERS)
    set_col_widths(ws, {
        1: 14, 2: 30,
        SIZE_START: 10, SIZE_START + 1: 11, SIZE_START + 2: 10,
        TOP_COL: 14, SUB_COL: 26,
        **{SEASON_START + i: 11 for i in range(len(SEASONS))},
    })
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(HEADERS))}1"

    # 示例行（按表头名定位，列顺序变化不影响）
    for col_idx_, header in enumerate(HEADERS, start=1):
        sized = SAMPLE_ROW_SIZED.get(header)
        if sized is not None:
            cell = ws.cell(row=2, column=col_idx_, value=sized)
            cell.fill = EXAMPLE_FILL
            cell.border = BORDER
            cell.alignment = CENTER
        no_size = SAMPLE_ROW_NO_SIZE.get(header)
        if no_size is not None:
            cell = ws.cell(row=3, column=col_idx_, value=no_size)
            cell.fill = EXAMPLE_FILL
            cell.border = BORDER
            cell.alignment = CENTER

    # 尺寸数值校验（Top/Height/Base 三列）
    dv_size = DataValidation(
        type="decimal",
        operator="greaterThanOrEqual",
        formula1="0",
        allow_blank=True,
        showErrorMessage=True,
    )
    dv_size.errorTitle = "格式不合法"
    dv_size.error = "请填数字（单位 cm）。Decorations / Greenhouse 两类请留空。"
    ws.add_data_validation(dv_size)
    dv_size.add(f"{get_column_letter(SIZE_START)}2:{get_column_letter(SIZE_END)}2000")

    # 一级分类下拉（内联 6 项）
    dv_top = DataValidation(
        type="list",
        formula1=f'"{",".join(TOP_LEVELS)}"',
        allow_blank=True,
        showErrorMessage=True,
    )
    dv_top.errorTitle = "分类不合法"
    dv_top.error = "请从下拉列表中选择 6 个一级分类之一。"
    dv_top.promptTitle = "第 1 步：选大类"
    dv_top.prompt = "先选一级分类，右侧二级分类会自动过滤。"
    ws.add_data_validation(dv_top)
    dv_top.add(f"{get_column_letter(TOP_COL)}2:{get_column_letter(TOP_COL)}2000")

    # 二级分类下拉（级联：=INDIRECT(SUBSTITUTE(一级分类单元格," ","_"))）
    dv_sub = DataValidation(
        type="list",
        formula1=f'=INDIRECT(SUBSTITUTE({get_column_letter(TOP_COL)}2," ","_"))',
        allow_blank=True,
        showErrorMessage=False,  # 一级还没选时不弹错误
    )
    dv_sub.promptTitle = "第 2 步：选小类"
    dv_sub.prompt = "先选左侧一级分类，这里会显示该类下的小类。"
    ws.add_data_validation(dv_sub)
    dv_sub.add(f"{get_column_letter(SUB_COL)}2:{get_column_letter(SUB_COL)}2000")

    # 季节/节日：只填 Yes（下拉仅 Yes 一项，其余留空）
    dv_yn = DataValidation(
        type="list",
        formula1='"Yes"',
        allow_blank=True,
        showErrorMessage=True,
    )
    dv_yn.errorTitle = "取值不合法"
    dv_yn.error = "只在对的季节列填 Yes，其余留空即可。"
    dv_yn.promptTitle = "勾选季节"
    dv_yn.prompt = "点选后填 Yes；不适用的季节留空（不用填 No）。"
    ws.add_data_validation(dv_yn)
    dv_yn.add(f"{get_column_letter(SEASON_START)}2:{get_column_letter(SEASON_END)}2000")


# --------------------------------------------------------------------------- #
# Sheet 3: Categories（对照 + 二级下拉数据源）
# --------------------------------------------------------------------------- #

def build_categories(ws) -> list[tuple[str, str]]:
    """写对照表，并返回 [(命名区域名, 引用范围), ...] 供二级下拉使用。"""
    ws.title = "Categories"
    cat_headers = ["二级分类（Subcategory）", "一级分类（Top）", "图片前缀", "图片命名示例"]
    style_header_row(ws, cat_headers)
    set_col_widths(ws, {1: 30, 2: 20, 3: 12, 4: 20})
    ws.freeze_panes = "A2"

    ranges: list[tuple[str, str]] = []
    row = 2
    for top, prefix, subs in CATEGORIES:
        start = row
        for sub in subs:
            ws.cell(row=row, column=1, value=sub).border = BORDER
            ws.cell(row=row, column=2, value=top).border = BORDER
            ws.cell(row=row, column=3, value=prefix).border = BORDER
            ws.cell(row=row, column=4, value=f"{prefix}1001.jpg").border = BORDER
            row += 1
        end = row - 1
        # 命名区域名与一级分类对应，空格转下划线（供 SUBSTITUTE→INDIRECT 查找）
        ranges.append((top.replace(" ", "_"), f"Categories!$A${start}:$A${end}"))

    # 尺寸留空的提示
    note_row = row + 1
    note = ws.cell(
        row=note_row, column=1,
        value="注：Decorations 与 Greenhouse 两类产品不填尺寸（Top/Height/Base 留空）。",
    )
    note.font = NOTE_FONT
    ws.merge_cells(start_row=note_row, start_column=1, end_row=note_row, end_column=4)

    return ranges


# --------------------------------------------------------------------------- #
# 主流程
# --------------------------------------------------------------------------- #

def main() -> None:
    wb = Workbook()
    build_instructions(wb.active)
    build_products(wb.create_sheet())
    ranges = build_categories(wb.create_sheet())

    # 每个一级分类一个命名区域（二级下拉的数据源）
    for name, ref in ranges:
        wb.defined_names.add(DefinedName(name, attr_text=ref))

    wb.save(OUTPUT)
    print(f"已生成: {OUTPUT}")
    print(f"  一级分类 {len(CATEGORIES)} 个 / 二级分类 {sum(len(s) for _, _, s in CATEGORIES)} 个")
    print(f"  季节 {len(SEASONS)} 个 / 主表 {len(HEADERS)} 列")
    print("  命名区域:", ", ".join(name for name, _ in ranges))


if __name__ == "__main__":
    main()
