import streamlit as st
import os

# 页面基本配置
st.set_page_config(
    page_title="AIA 智能工作平台",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 侧边栏导航
st.sidebar.title("AIA 智能助手导航")
app_mode = st.sidebar.selectbox(
    "请选择功能模块",
    [
        "🏠 平台首页", 
        "💬 智能问答与条例检索", 
        "🤝 辅助见客 (实时应对)", 
        "🎤 话术训练 (AI模拟演练)", 
        "📊 一键生成PPT大纲"
    ]
)

# 模块一：平台首页
if app_mode == "🏠 平台首页":
    st.title("欢迎使用 AIA 内部智能工作平台 🚀")
    st.markdown("""
    本平台旨在通过 AI 技术赋能团队日常展业，主要功能包括：
    * **智能问答与条例检索**：快速查询保险条款与历史案例。
    * **辅助见客**：在客户沟通现场提供即时策略与产品亮点支持。
    * **话术训练**：与 AI 进行模拟演练，提升异议处理能力。
    * **一键生成PPT**：快速输出面向客户的演示文稿结构。
    """)
    st.info("💡 提示：请从左侧边栏选择您需要使用的功能模块。")

# 模块二：智能问答与条例检索
elif app_mode == "💬 智能问答与条例检索":
    st.title("📚 保险条例与案例知识库")
    query = st.text_input("请输入您想查询的保险条款、理赔案例或产品问题：")
    if st.button("开始检索"):
        if query:
            st.success("检索结果：")
            st.write(f"针对您的问题“{query}”，系统正在从AIA条例资料库中匹配相关条款...")
            st.info("（当前为演示版本，后续可接入真实保单及条例向量库）")
        else:
            st.warning("请输入查询内容。")

# 模块三：辅助见客
elif app_mode == "🤝 辅助见客 (实时应对)":
    st.title("🎯 见客实时辅助")
    client_situation = st.text_area("输入当前客户的顾虑或提出的尖锐问题（例如：觉得重疾险太贵、对比了其他竞品）：")
    if st.button("生成应对策略"):
        if client_situation:
            st.markdown("### 💡 AI 建议话术与应对策略：")
            st.write("1. **共情与肯定**：首先认可客户对预算的合理关切，建立信任关系。")
            st.write("2. **价值重塑**：强调AIA产品的独特优势及长期保障的杠杆效应，避免陷入单纯的价格战。")
            st.write("3. **促成话术**：用实际理赔案例或精算数据打消客户顾虑。")
        else:
            st.warning("请输入客户当前的情况。")

# 模块四：话术训练
elif app_mode == "🎤 话术训练 (AI模拟演练)":
    st.title("👥 模拟见客演练（Roleplay）")
    persona = st.selectbox("选择客户画像", ["精打细算的年轻白领", "注重资产配置的企业主", "担心健康风险的中年父母"])
    st.write(f"当前模拟对象：**{persona}**。您可以直接在下方输入您的开场白或推销话术，AI将扮演该客户进行真实回应。")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("请输入您的推销话术..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            ai_response = f"（模拟{persona}的回应）：“听起来挺不错的，不过我想知道如果万一发生了理赔，具体流程会不会很繁琐呢？”"
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

# 模块五：一键生成PPT大纲
elif app_mode == "📊 一键生成PPT大纲":
    st.title("📑 客户专属 PPT 结构生成器")
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("客户称呼", value="张先生/女士")
        client_goal = st.text_input("客户核心需求", value="子女教育金与重疾保障")
    with col2:
        budget = st.text_input("大致预算区间", value="年缴 5 万港币")
        product_focus = st.text_input("倾向推介的产品类型", value="储蓄分红险 + 多重守护重疾险")

    if st.button("生成 PPT 大纲与演讲备注"):
        st.success("PPT 结构生成成功！")
        st.markdown(f"""
        ### 🎯 为 **{client_name}** 定制的演示文稿大纲：
        * **Slide 1**：封面（致 {client_name} 的专属财富与健康保障规划方案）
        * **Slide 2**：当前财务现状分析与风险敞口（聚焦 {client_goal}）
        * **Slide 3**：核心解决方案与组合建议（主推：{product_focus}）
        * **Slide 4**：AIA 百年品牌实力与稳健分红实现率展示
        * **Slide 5**：保费预算规划（基于 {budget} 的资金分配与现金价值增长曲线）
        * **Slide 6**：下一步行动建议与专属签约权益
        """)