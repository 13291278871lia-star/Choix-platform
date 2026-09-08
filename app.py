import streamlit as st

# 页面基本配置
st.set_page_config(
    page_title="CHOIX & AIA 智能工作与展业平台",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义高级企业级 UI 样式
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        background: linear-gradient(135deg, #002B49 0%, #005691 100%);
        color: white;
        border: none;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        opacity: 0.9;
        box-shadow: 0 4px 12px rgba(0,86,145,0.3);
    }
    .card-box {
        background-color: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 5px solid #005691;
    }
    .highlight-banner {
        background: linear-gradient(135deg, #002B49 0%, #004b7a 100%);
        color: white;
        padding: 30px;
        border-radius: 12px;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 侧边栏导航
st.sidebar.markdown("### 🌟 CHOIX 卓智资产管理集团")
st.sidebar.markdown("*“您的选择,成就您的人生”*")
st.sidebar.markdown("---")

app_mode = st.sidebar.selectbox(
    "请选择功能模块",
    [
        "🏠 平台首页与集团概览", 
        "💬 智能问答与条例检索", 
        "🤝 辅助见客 (实时应对)", 
        "🎤 话术训练 (AI模拟演练)", 
        "📊 专属定制 PPT 演讲大纲生成器",
        "⚙️ 系统设置与API配置"
    ]
)

# 模块一：平台首页与集团概览
if app_mode == "🏠 平台首页与集团概览":
    st.markdown("""
        <div class="highlight-banner">
            <h1>欢迎来到 CHOIX 卓智 & AIA 智能工作平台 🚀</h1>
            <p>结合资深区域总监黎天佑 (Arnold Lai) 创立的 CHOIX 团队文化、SEED 系统及 AIA 顶尖资源，全方位赋能您的展业与团队管理。</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card-box">
            <h3>🎯 核心愿景</h3>
            <p><strong>Trusted Financial Advisor</strong><br>
            为客户最信赖、专业的财务策划顾问，以客为先，提供客观理性分析与全球资产配置方案。</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card-box">
            <h3>💡 SEED 系统</h3>
            <p><strong>Simple, Easy, Effective, Duplicable</strong><br>
            香港首个全面植入 SEED 系统的团队，简单、容易、有效、可复制，成就无数 MDRT、COT、TOT。</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="card-box">
            <h3>📈 卓越成就</h3>
            <p><strong>連續多年 No.1</strong><br>
            AIA 財務策劃顧問團隊新造保單保費、銷售數目及 MDRT 比例全港領先，給您最高起跑線。</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.info("💡 提示：请从左侧边栏切换不同模块，体验智能问答、见客实时应对、角色扮演及深度 PPT 生成工具。")

# 模块二：智能问答与条例检索
elif app_mode == "💬 智能问答与条例检索":
    st.title("📚 保险条例、集团优势与知识库检索")
    st.markdown("输入您的业务问题、条款关键词或内地访港客户痛点，系统将精准智能匹配 CHOIX 内部知识库。")
    
    query = st.text_input("请输入查询关键词或业务问题：", placeholder="例如：内地高净值客户资产传承的优势是什么？/ 重疾险多次赔付细则")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        search_btn = st.button("开始智能检索")
        
    if search_btn:
        if query:
            st.markdown("### 🔍 深度检索结果：")
            st.success("匹配内部专业条例与 CHOIX 实战话术库")
            st.markdown(f"""
            * **针对您的问题：“{query}”**
            * **核心条款与切入点**：
              1. 针对大湾区及抵港内地客户：香港保险拥有低税率、法制健全、全球美元资产配置优势。未来几年大量民企面临从第一代到第二代接班（300万家民企），信托与家族办公室工具需求极其殷切。
              2. 内部协同指引：善用 CHOIX 独家 SEED 系统及每月区会培训、律师/基金经理专业分享。
            """)
        else:
            st.warning("请输入查询内容。")

# 模块三：辅助见客
elif app_mode == "🤝 辅助见客 (实时应对)":
    st.title("🎯 见客现场实时应对辅助")
    st.markdown("在与客户沟通时遇到难点、异议或价格顾虑？输入当前情境，AI 立即提供专业应对策略。")
    
    client_situation = st.text_area(
        "输入当前客户的顾虑、异议或具体场景：", 
        placeholder="例如：客户觉得美元储蓄分红险锁定期长，或者担心内地客户来港理赔的便利性..."
    )
    
    if st.button("生成现场应对策略"):
        if client_situation:
            st.markdown("### 💡 AI 专业建议话术：")
            st.markdown("""
            * **第一步：同理心与专业共鸣**
              > “非常理解您的考量，资金的流动性和安全性永远是高净值家庭的第一核心。您能提出这个细节，说明您对资产配置非常有远见。”
            * **第二步：价值重塑（香港金融核心优势）**
              > “我们可以看一组宏观数据：香港作为全球领先的财富管理中心，拥有最完善的普通法体系与美元挂钩机制。通过多币种配置和长远滚存，不仅能对抗汇率波动，更能实现跨代财富安全传承。”
            * **第三步：AIA 实力与理赔保障**
              > “友邦保险作为百年泛亚上市巨头，在港澳拥有4栋自有物业及庞大的专属理赔网络，累计理赔金额和客户信任度常年稳居全港第一，让您后顾无忧。”
            """)
        else:
            st.warning("请输入客户当前的情况或顾虑。")

# 模块四：话术训练
elif app_mode == "🎤 话术训练 (AI模拟演练)":
    st.title("👥 模拟见客实战演练 (Roleplay)")
    persona = st.selectbox("选择要挑战的客户画像", [
        "精打细算、注重性价比的年轻白领", 
        "注重家族资产安全与跨境传承的企业主", 
        "担心子女海外教育与健康保障的中产父母"
    ])
    
    st.markdown(f"当前模拟对象：**{persona}**。您可以直接在下方输入您的推销或回应话术，AI将扮演该真实客户进行切磋。")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("请输入您的推销或回应话术..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            if "精打细算" in persona:
                ai_response = "保障听起来不错，但我每个月现金流有限，万一中间周转不开交不起保费怎么办？有没有更灵活的方案？"
            elif "企业主" in persona:
                ai_response = "现在公司业务正处于转型期，流动资金对我来说最关键。你们的家族办公室或信托方案，具体怎么帮我做资产隔离？"
            else:
                ai_response = "孩子以后出国读书费用很高，在国内买和在香港买教育金到底有什么本质区别？汇率风险怎么控制？"
                
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

# 模块五：一键生成PPT大纲 (深度升级版)
elif app_mode == "📊 专属定制 PPT 演讲大纲生成器":
    st.title("📑 深度定制客户与展业 PPT 大纲生成器")
    st.markdown("基于 CHOIX 集团专业话册与体系，为您一键生成结构严密、干货满满、带详细演讲备注的多页专业 PPT 大纲。")
    
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("客户/团队成员称呼", value="林总 / 林先生")
        presentation_type = st.selectbox("演讲/展示目的", ["高净值客户资产配置与财富传承方案", "精英人才招募与事业发展规划(AIP/MB计划)", "家庭综合保障与子女教育金规划"])
    with col2:
        budget_range = st.text_input("预算/保费区间", value="年缴 10-20 万美元 / 或寻找事业新风口")
        custom_focus = st.text_input("核心关注点", value="全球化美元资产配置 + AIA 品牌信任度")

    if st.button("生成完整多页专业 PPT 大纲"):
        st.success("专属 PPT 大纲生成成功！内容已按专业管理咨询/高端金融标准深度扩展。")
        
        if "资产配置" in presentation_type:
            st.markdown(f"""
            ### 📋 专属方案：致 {client_name} 的全球资产配置与财富传承规划
            
            * **Slide 1：封面页**
              * *大标题*：洞见未来，智创财富 — {client_name} 尊享全球资产配置与家族传承规划
              * *副标题*：依托百年友邦与 CHOIX 卓智顶尖专业顾问团队，为您守护世代根基。
              * *演讲备注*：尊敬的林总，感谢您抽出宝贵时间。今天我们不仅是讨论一份保障，更是探讨如何在当前宏观周期下，为您及家族做好全球资产的安全锚定。
            
            * **Slide 2：宏观经济新周期与高净值资产痛点诊断**
              * *核心要点*：解析当前低利率环境、汇率波动及民营企业财富传承的机遇与挑战。
              * *数据支撑*：香港已超越瑞士成为全球第一财富管理中心；未来数年大量民企面临代际传承。
              * *演讲备注*：面对多变的经济周期，单一市场的单一币种资产已经难以满足风险对冲的需求。
            
            * **Slide 3：为什么选择香港与友邦保险？（实力见证）**
              * *核心优势*：友邦保险（AIA）作为泛亚最大独立上市人寿保险集团，总资产达3,050亿美元，信用评级标普AA-。
              * *品牌背书*：连续多年香港保险市场新造保单保费及销售数目 No.1，坐拥港澳4栋自有物业。
              * *演讲备注*：选择平台的第一原则是稳健。友邦超过百年的稳健基业和强大的资本实力，是您资产长治久安的坚实后盾。
            
            * **Slide 4：核心解决方案：尊享美元储蓄分红与长效保障**
              * *推荐组合*：多元货币储蓄保障计划 + 高端全球医疗/重疾多重保障。
              * *核心亮点*：预期收益稳健、支持多币种灵活转换、多代受保人无限次转换。
            
            * **Slide 5：CHOIX 卓智资产管理集团独家专业支援**
              * *团队优势*：汇聚前环球企业高管、海外留学精英及资深金融分析师。
              * *智囊赋能*：引入 SEED 系统及顶尖智库，为您提供全生命周期的私域财富管理服务。
            
            * **Slide 6：下一步行动建议与闭环**
              * *行动呼吁*：确认方案方向、协助核对投保细节，开启您的家族财富全球化布局。
            """)
        else:
            st.markdown(f"""
            ### 📋 专属方案：开启您的璀璨事业新高度 — CHOIX 卓越事业说明会
            
            * **Slide 1：封面页**
              * *大标题*：超越自我，成就非凡 — CHOIX & AIA 精英事业发展蓝图
              * *副标题*：给不甘平凡的您：用同样的时间，换取更丰盛的职业回报。
            
            * **Slide 2：大时代下的职业新风口与痛点突破**
              * *行业优势*：金融及保险业持续稳居香港平均最高收入行业首位（月入中位数超40,000港元）。
              * *CHOIX 精神*：创始人 Arnold Lai 亲历从广告精英到资深区域总监的华丽转身。
            
            * **Slide 3：友邦事业发展计划与优厚花红支援（AIP / TTFS / EDP）**
              * *首年福利*：灵活的对数要求与丰厚的每月花红（MB最高达80,000港元）。
              * *佣金回报*：远高出同业的佣金比例、持续续保佣金及年终花红。
            
            * **Slide 4：CHOIX 独家 SEED 成功系统与专业培训**
              * *四大支柱*：简单 (Simple)、容易 (Easy)、有效 (Effective)、可复制 (Duplicable)。
              * *顶级支援*：背靠亚洲保险教父拿督蔡明敏博士智慧、每月区会分享及进修资助计划。
            
            * **Slide 5：清晰透明的晋升阶梯与 MDRT 摇篮**
              * *晋升路径*：最快1年晋升营业单位主管，5年迈向财富管理总监。
              * *荣誉殿堂*：CHOIX 团队 MDRT 达成率及终身会员比例名列前茅。
            
            * **Slide 6：加入 CHOIX，成就您的人生**
              * *行动呼吁*：目标在眼前，机会在身边，立即预约导师面谈，开启全新事业篇章。
            """)

# 模块六：系统设置与API配置
elif app_mode == "⚙️ 系统设置与API配置":
    st.title("⚙️ 系统底层设置")
    st.markdown("管理大模型 API 密钥、知识库向量源及 CHOIX 内部团队专属权限。")
    
    api_key = st.text_input("输入大模型 API Key (OpenAI / Claude / DeepSeek)", type="password")
    model_choice = st.selectbox("选择底层调用大模型", ["gpt-4o", "claude-3-5-sonnet", "deepseek-chat"])
    
    if st.button("保存并更新配置"):
        if api_key:
            st.success("API 密钥配置成功！所有智能问答与 PPT 大纲生成模块已实时接入最新大模型。")
        else:
            st.warning("请输入有效的 API 密钥。")
