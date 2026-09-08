import streamlit as st
import datetime

# 页面基本配置
st.set_page_config(
    page_title="CHOIX 卓智智能工作平台",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义 CSS 样式美化卡片和交互
st.markdown("""
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 2rem;
    }
    .card-box {
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid #E5E7EB;
        background-color: #FFFFFF;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        height: 100%;
        transition: all 0.3s ease;
    }
    .card-box:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border-color: #93C5FD;
    }
    </style>
""", unsafe_allow_html=True)

# 侧边栏导航
st.sidebar.markdown("### 🌟 CHOIX 卓智资产管理集团")
st.sidebar.markdown("*您的选择,成就您的人生*")
st.sidebar.markdown("---")

menu_option = st.sidebar.radio(
    "请选择功能模块",
    [
        "平台首页与集团概览",
        "智能问答与条例检索",
        "辅助见客 (实时应对)",
        "话术训练 (AI模拟演练)",
        "专属定制 PPT 演讲大纲生成器",
        "系统设置与API配置"
    ]
)

# 初始化页面状态（用于首页卡片点击直接跳转）
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "平台首页与集团概览"

if menu_option != st.session_state.active_tab and menu_option != "平台首页与集团概览":
    st.session_state.active_tab = menu_option

# ==================== 1. 平台首页与集团概览 ====================
if menu_option == "平台首页与集团概览" or st.session_state.active_tab == "平台首页与集团概览":
    st.markdown('<p class="main-title">欢迎来到 CHOIX 卓智智能工作平台 🚀</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">全方位赋能您的展业、资产配置与团队管理。</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="card-box">
                <h3>🎯 核心愿景</h3>
                <p><b>Trusted Financial Advisor</b><br>为客户最信赖、专业的财务策划顾问，以客户为先，提供客观理性分析与全球资产配置方案。</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("进入 智能问答系统", use_container_width=True):
            st.session_state.active_tab = "智能问答与条例检索"
            st.rerun()

    with col2:
        st.markdown("""
            <div class="card-box">
                <h3>💡 SEED 系统</h3>
                <p><b>Simple, Easy, Effective, Duplicable</b><br>简单、容易、有效、可复制，成就无数 MDRT、COT、TOT。</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("进入 辅助见客模块", use_container_width=True):
            st.session_state.active_tab = "辅助见客 (实时应对)"
            st.rerun()

    with col3:
        st.markdown("""
            <div class="card-box">
                <h3>📈 卓越成就</h3>
                <p><b>行业领先</b><br>顶尖资产管理与卓越团队孵化基地，给您最高起跑线与专业赋能。</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("使用 PPT 演讲大纲生成器", use_container_width=True):
            st.session_state.active_tab = "专属定制 PPT 演讲大纲生成器"
            st.rerun()

    st.markdown("---")
    st.info("💡 提示：点击上方卡片底部的按钮或通过左侧边栏，即可快速进入对应功能模块。")

# ==================== 2. 智能问答与条例检索 ====================
elif menu_option == "智能问答与条例检索":
    st.markdown("### 🔍 智能问答与条例检索")
    st.write("输入您在展业或管理中遇到的合规、产品、税务或政策问题，AI 将为您精准检索并解答。")
    
    query = st.text_input("请输入您想查询的问题：", placeholder="例如：大湾区个人养老金税收优惠政策是什么？")
    if st.button("开始检索", type="primary"):
        if query:
            with st.spinner("正在检索内部智库与条例..."):
                # 模拟输出
                st.success("检索完成：")
                st.markdown(f"> **查询结果：** 关于“{query}”的条例说明符合 CHOIX 标准展业规范。建议结合最新合规指引与客户实际资产状况进行说明。")
        else:
            st.warning("请输入有效的问题内容。")

# ==================== 3. 辅助见客 (实时应对) ====================
elif menu_option == "辅助见客 (实时应对)":
    st.markdown("### ⚡ 辅助见客 (实时应对)")
    st.write("在与客户面谈或连线时，输入客户的异议或核心关切，获取即时专业应对策略。")
    
    client_objection = st.text_area("客户当前提出的异议或关注点：", placeholder="例如：客户担心目前的全球宏观经济波动，对海外资产配置持观望态度。")
    if st.button("获取应对策略", type="primary"):
        if client_objection:
            with st.spinner("AI 正在生成黄金话术..."):
                st.markdown("#### 💡 推荐应对策略与话术：")
                st.markdown("1. **共情与肯定**：认可客户对风险的敏锐度，稳住客户情绪。")
                st.markdown("2. **专业切入**：利用全球分散投资理论，说明资产配置如何对冲单一市场波动。")
                st.markdown("3. **成功案例**：分享类似高净值客户通过多元配置实现穿越周期的稳健收益。")
        else:
            st.warning("请填写客户异议内容。")

# ==================== 4. 话术训练 (AI模拟演练) ====================
elif menu_option == "话术训练 (AI模拟演练)":
    st.markdown("### 🎙️ 话术训练 (AI模拟演练)")
    st.write("选择模拟场景，由 AI 扮演高净值客户或异议客户，帮您打磨销售与沟通话术。")
    
    scenario = st.selectbox("选择演练场景", ["高净值客户资产配置面谈", "大额保单异议处理", "团队招募与面谈沟通"])
    if st.button("开始模拟对话"):
        st.info(f"已为您启动【{scenario}】模拟。AI 客户已上线，您可以直接在下方输入您的开场白：")
    
    user_speech = st.text_input("您的发言：")
    if user_speech:
        st.markdown(f"**您**：{user_speech}")
        st.markdown(f"**AI 客户/评委反馈**：沟通语气专业，逻辑清晰。建议可以更多地关注客户的资产安全痛点。")

# ==================== 5. 专属定制 PPT 演讲大纲生成器 ====================
elif menu_option == "专属定制 PPT 演讲大纲生成器":
    st.markdown("### 📊 专属定制 PPT 演讲大纲及草稿生成器")
    st.write("输入您的演讲主题或分享需求，一键生成结构化大纲，并可直接导出 PPT 草稿文件用于排版！")

    topic = st.text_input("演讲主题 / 客户分享会主题：", value="高净值客户的全球资产配置与财富传承")
    target_audience = st.selectbox("目标受众", ["高净值个人/企业家", "潜在团队合伙人/新人", "内部团队专业培训"])
    slides_count = st.slider("期望页数", 5, 15, 8)

    if st.button("生成 PPT 大纲与草稿内容", type="primary"):
        with st.spinner("正在为您编排专业演讲大纲与草稿..."):
            st.success("生成成功！")
            
            # 动态生成大纲内容
            ppt_content = f"""
# 演讲主题：{topic}
## 听众定位：{target_audience}
---
### Page 1: 封面
- 主标题：{topic}
- 副标题：CHOIX 卓智资产管理集团 专业分享会
- 讲师：CHOIX 资深财务策划顾问

### Page 2: 目录与宏观背景
- 1. 当前宏观经济与全球资产配置新趋势
- 2. 高净值客户面临的典型痛点与风险解析
- 3. CHOIX 核心资产配置逻辑与解决方案
- 4. 真实成功案例分享与总结

### Page 3-5: 核心内容拆解
- 阐述多元化分散投资的必要性
- 介绍通过专业工具实现财富隔离、传承与增值
- 结合 SEED 系统理念展现专业服务的可复制性与安心保障

### Page 6: 互动与答疑 (Q&A)
- 感谢聆听，开启现场专属咨询与交流
"""
            st.markdown(ppt_content)
            
            # 提供下载 PPT 草稿功能
            st.download_button(
                label="📥 下载 PPT 大纲草稿 (.txt)",
                data=ppt_content,
                file_name=f"CHOIX_PPT_Draft_{datetime.date.today()}.txt",
                mime="text/plain"
            )

# ==================== 6. 系统设置与API配置 ====================
elif menu_option == "系统设置与API配置":
    st.markdown("### ⚙️ 系统设置与 API 配置")
    st.write("管理大模型接口密钥、系统偏好以及缓存数据。")
    
    api_key = st.text_input("OpenAI / 专属大模型 API Key", type="password", value="sk-xxxxxxxxxxxxxxxxxxxxxxxx")
    model_choice = st.selectbox("选择默认 AI 模型", ["GPT-4o", "Claude 3.5 Sonnet", "CHOIX Custom LLM"])
    
    if st.button("保存设置", type="save"):
        st.success("配置已成功更新！")
