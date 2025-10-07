function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
    
    if (!toastComponent) return;

    toastComponent.classList.remove(
        'bg-red-100', 'border-red-500', 'text-red-600',
        'bg-green-100', 'border-green-500', 'text-green-600',
        'bg-blue-100', 'border-blue-500', 'text-blue-600',
        'bg-purple-100', 'border-purple-500', 'text-purple-600',
        'bg-white', 'border-white/20', 'text-white'
    );

    if (type === 'success') {
        toastComponent.classList.add('bg-green-100', 'border-green-500', 'text-green-600');
        toastComponent.style.border = '1px solid rgba(34, 197, 94, 0.8)';
        toastIcon.innerHTML = '✅';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-100', 'border-red-500', 'text-red-600');
        toastComponent.style.border = '1px solid rgba(239, 68, 68, 0.8)';
        toastIcon.innerHTML = '❌';
    } else if (type === 'info') {
        toastComponent.classList.add('bg-blue-100', 'border-blue-500', 'text-blue-600');
        toastComponent.style.border = '1px solid rgba(59, 130, 246, 0.8)';
        toastIcon.innerHTML = 'ℹ️';
    } else {
        toastComponent.classList.add('bg-white', 'border-white/20', 'text-white');
        toastComponent.style.border = '1px solid rgba(255, 255, 255, 0.2)';
        toastIcon.innerHTML = '💬';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}
