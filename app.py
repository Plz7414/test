#安裝插件皆在packages.md
#記帳功能撰寫-蔡騰逸 UI/UX設計-丁仲恩 可愛擔當-劉紘安
#使用方法按三角形執行後再Terminal輸入 streamlit run app.py
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Python 程式設計 期末專題",
    layout="wide",
)

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei",
    "PMingLiU",
    "MingLiU",
    "Arial Unicode MS",
    "Heiti TC",
]
plt.rcParams["axes.unicode_minus"] = False


def analyze_expenses(data_frame, target_year, target_month, user_budgets, category_mapping):
    st.markdown(f"###  {target_year} 年 {target_month} 月 記帳分析與消費警示")

    df_ts = data_frame.copy()
    df_ts["日期"] = pd.to_datetime(df_ts["日期"])
    df_ts.set_index("日期", inplace=True)

    monthly_df = df_ts[
        (df_ts.index.year == target_year) & (df_ts.index.month == target_month)
        ]

    if monthly_df.empty:
        st.warning(f"❌ 警告：在 {target_year}/{target_month} 找不到任何消費紀錄！")
        return

    monthly_df["中文類別"] = monthly_df["類別"].map(category_mapping)
    category_totals = monthly_df.groupby("中文類別")["金額"].sum()

    st.subheader("【 當月消費審查與警示 】")

    for cat_en, budget in user_budgets.items():
        cat_zh = category_mapping[cat_en]
        actual = category_totals.get(cat_zh, 0)
        percentage = (actual / budget) * 100 if budget > 0 else 0

        if actual > budget:
            st.error(
                f"🚨 🛑 **【💥 嚴重超標】[{cat_zh}] 類別**：目前已花費 ${actual:,} / 預算 ${budget:,} ({percentage:.1f}%) \n"
                f"👉 *警告：老兄別吃了/別玩了！已經超支 ${actual - budget:,}，準備吃土。*"
            )
        elif percentage >= 80:
            st.warning(
                f"⚠️ **【🟡 緊繃警告】[{cat_zh}] 類別**：目前已花費 ${actual:,} / 預算 ${budget:,} ({percentage:.1f}%) \n"
                f"👉 *提示：距離破產只剩 ${budget - actual:,}，請克制物慾。*"
            )
        else:
            st.success(
                f"✅ **【🟢 安全】[{cat_zh}] 類別**：目前已花費 ${actual:,} / 預算 ${budget:,} ({percentage:.1f}%)"
            )

    st.markdown("---")

    fig, axes = plt.subplots(1, 2, figsize=(15, 6), clear=True)

    present_categories = category_totals.index
    axes[0].pie(
        category_totals,
        labels=present_categories,
        autopct="%1.1f%%",
        startangle=140,
        colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"],
    )
    axes[0].set_title(f"{target_month}月 各類別消費比例", fontsize=14)

    daily_totals = monthly_df.groupby(monthly_df.index.date)["金額"].sum()
    cumulative_totals = daily_totals.cumsum()

    axes[1].plot(
        daily_totals.index,
        daily_totals.values,
        marker="o",
        label="每日消費金額",
        color="#1f77b4",
        linestyle="--",
    )
    axes[1].plot(
        cumulative_totals.index,
        cumulative_totals.values,
        marker="s",
        label="當月累積花費",
        color="#d62728",
    )

    axes[1].set_title(f"{target_month}月 每日消費與累積趨勢", fontsize=14)
    axes[1].set_xlabel("日期")
    axes[1].set_ylabel("金額 (元)")
    axes[1].grid(True, linestyle=":", alpha=0.6)
    axes[1].legend()

    fig.autofmt_xdate()
    plt.tight_layout()

    st.pyplot(fig)
    plt.close(fig)


if "expense_list" not in st.session_state:
    st.session_state.expense_list = []

category_mapping = {"e": "食", "c": "衣", "l": "住", "t": "行", "f": "娛樂"}


st.title("Python 程式設計 期末專題")
st.caption("用精美的網頁介面幫你控制預算、遠離吃土命運。")

with st.sidebar:
    st.header("步驟 1：設定每月預算")
    user_budgets = {}
    for cat_en, cat_zh in category_mapping.items():
        user_budgets[cat_en] = st.number_input(
            f"[{cat_zh}] 預算金額", min_value=0, value=5000, step=500, key=f"budget_{cat_en}"
        )

    st.markdown("---")
    st.header("快速匯入歷史紀錄")

    sample_csv_data = (
        "日期,類別,金額\n"
        "2026-01-02,e,150\n"
        "2026-01-10,f,1500\n"
        "2026-02-12,c,790\n"
        "2026-02-15,l,6500\n"
        "2026-03-12,c,2400\n"
        "2026-03-18,f,990"
    )
    st.download_button(
        label="下載標準範例 CSV 檔案",
        data=sample_csv_data,
        file_name="example_expenses.csv",
        mime="text/csv",
    )

    if st.button(" 一鍵載入 2026 年 1-3 月示範資料", width="stretch"):
        demo_records = [
            {"日期": "2026-01-02", "類別": "e", "金額": 150},
            {"日期": "2026-01-05", "類別": "t", "金額": 60},
            {"日期": "2026-01-10", "類別": "f", "金額": 1500},
            {"日期": "2026-01-15", "類別": "l", "金額": 6500},
            {"日期": "2026-01-18", "類別": "e", "金額": 450},
            {"日期": "2026-01-22", "類別": "c", "金額": 1280},
            {"日期": "2026-01-28", "類別": "t", "金額": 120},
            {"日期": "2026-02-01", "類別": "e", "金額": 85},
            {"日期": "2026-02-04", "類別": "t", "金額": 45},
            {"日期": "2026-02-08", "類別": "f", "金額": 650},
            {"日期": "2026-02-12", "類別": "c", "金額": 790},
            {"日期": "2026-02-15", "類別": "l", "金額": 6500},
            {"日期": "2026-02-19", "類別": "e", "金額": 320},
            {"日期": "2026-02-25", "類別": "t", "金額": 200},
            {"日期": "2026-02-28", "類別": "f", "金額": 350},
            {"日期": "2026-03-03", "類別": "e", "金額": 110},
            {"日期": "2026-03-07", "類別": "t", "金額": 85},
            {"日期": "2026-03-12", "類別": "c", "金額": 2400},
            {"日期": "2026-03-15", "類別": "l", "金額": 6500},
            {"日期": "2026-03-18", "類別": "f", "金額": 990},
            {"日期": "2026-03-22", "類別": "e", "金額": 560},
            {"日期": "2026-03-26", "類別": "t", "金額": 70},
            {"日期": "2026-03-30", "類別": "c", "金額": 450}
        ]
        st.session_state.expense_list.extend(demo_records)
        st.success("成功載入 23 筆 2026年1-3月 的示範消費紀錄！")
        st.rerun()

    st.caption("或是你也可以自行上傳：")
    uploaded_file = st.file_uploader("上傳消費紀錄 CSV 檔", type=["csv"], label_visibility="collapsed")

    if uploaded_file is not None:
        try:
            uploaded_df = pd.read_csv(uploaded_file)
            required_cols = ["日期", "類別", "金額"]

            if all(col in uploaded_df.columns for col in required_cols):
                if st.button("確認匯入 CSV 資料", width="stretch"):
                    uploaded_df["日期"] = uploaded_df["日期"].astype(str)
                    uploaded_df["類別"] = uploaded_df["類別"].astype(str).str.lower()
                    uploaded_df["金額"] = uploaded_df["金額"].astype(int)

                    csv_records = uploaded_df[required_cols].to_dict(orient="records")
                    st.session_state.expense_list.extend(csv_records)
                    st.success(f"🎉 成功匯入 {len(csv_records)} 筆消費紀錄！")
                    st.rerun()
            else:
                st.error("❌ CSV 格式錯誤！必須包含：日期、類別、金額 三個欄位。")
        except Exception as e:
            st.error(f"❌ 檔案讀取失敗：{str(e)}")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("步驟 2：新增消費紀錄")
    input_date = st.date_input("選擇日期", datetime.date.today())
    input_cat = st.selectbox(
        "選擇類別",
        options=list(category_mapping.keys()),
        format_func=lambda x: f"{x} : {category_mapping[x]}",
    )
    input_amount = st.number_input("輸入金額", min_value=1, value=100, step=10)

    if st.button("成功記帳", width="stretch"):
        new_record = {
            "日期": input_date.strftime("%Y-%m-%d"),
            "類別": input_cat,
            "金額": int(input_amount),
        }
        st.session_state.expense_list.append(new_record)
        st.toast(f"✅ 已紀錄：{category_mapping[input_cat]} 花費 ${input_amount}")

with col2:
    st.subheader("目前記帳歷史紀錄")
    if st.session_state.expense_list:
        df_show = pd.DataFrame(st.session_state.expense_list)
        df_show["類別"] = df_show["類別"].map(category_mapping)
        st.dataframe(df_show, height=200)

        if st.button("🧹 清除所有紀錄"):
            st.session_state.expense_list = []
            st.rerun()
    else:
        st.info("目前還沒有任何記帳紀錄，請從左側新增或上傳 CSV！")

st.markdown("---")

st.subheader("步驟 3：分析看板")

if st.session_state.expense_list:
    col_y, col_m = st.columns(2)
    with col_y:
        target_year = st.number_input("想分析的年份", min_value=2000, max_value=2100, value=2026)
    with col_m:
        target_month = st.number_input("想分析的月份", min_value=1, max_value=12, value=1)

    df_user = pd.DataFrame(st.session_state.expense_list)
    analyze_expenses(df_user, target_year, target_month, user_budgets, category_mapping)
else:
    st.warning("請先在上方新增至少一筆消費資料，才會啟動分析圖表功能。")