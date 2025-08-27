'use client';

import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';

// Placeholder for viewing all polls
export default function PollsPage() {
  const { session } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!session) {
      router.push('/auth');
    }
  }, [session, router]);

  if (!session) {
    return null;
  }

  return <div className="container mx-auto py-8">Polls list coming soon.</div>;
}
