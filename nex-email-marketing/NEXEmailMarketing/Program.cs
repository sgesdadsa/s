using System;
using System.Windows.Forms;

namespace NEXEmailMarketing
{
    internal static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // Exibe aviso legal na primeira execução
            var termsAccepted = Properties.Settings.Default.TermsAccepted;

            if (!termsAccepted)
            {
                var result = MessageBox.Show(
                    "AVISO LEGAL - NEX Email Marketing Pro\n\n" +
                    "✅ Esta ferramenta deve ser usada APENAS para email marketing LEGÍTIMO\n\n" +
                    "VOCÊ DEVE:\n" +
                    "✅ Ter consentimento explícito dos destinatários (opt-in)\n" +
                    "✅ Incluir link de unsubscribe em todos os emails\n" +
                    "✅ Respeitar leis anti-spam (CAN-SPAM, LGPD, GDPR)\n" +
                    "✅ Usar apenas para seu próprio negócio/empresa\n\n" +
                    "PROIBIDO:\n" +
                    "❌ Enviar spam para listas compradas\n" +
                    "❌ Enviar emails sem consentimento\n" +
                    "❌ Usar para fraude, phishing ou atividades ilegais\n\n" +
                    "Ao clicar em OK, você aceita usar esta ferramenta de forma ética e legal.\n\n" +
                    "Você aceita estes termos?",
                    "Termos de Uso - LEIA ANTES DE USAR",
                    MessageBoxButtons.OKCancel,
                    MessageBoxIcon.Warning
                );

                if (result != DialogResult.OK)
                {
                    MessageBox.Show(
                        "Você deve aceitar os termos para usar o NEX Email Marketing.",
                        "Termos Não Aceitos",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Information
                    );
                    return;
                }

                Properties.Settings.Default.TermsAccepted = true;
                Properties.Settings.Default.Save();
            }

            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
