'use client';

import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';

// Placeholder for creating a new poll
export default function NewPollPage() {
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

  return <div className="container mx-auto py-8">New poll form coming soon.</div>;
}
